/*
**  Copyright (C) Optumi Inc - All rights reserved.
**
**  You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
**  To receive a copy of the licensing terms please write to contact@optumi.com or visit us at http://www.optumi.com.
**/

import { Global } from '../Global';

import { ISignal, Signal } from '@lumino/signaling';

import FileServerUtils from '../utils/FileServerUtils';
import { ServerConnection } from '@jupyterlab/services';
import { FileMetadata } from '../components/deploy/fileBrowser/FileBrowser';

class FileProgress {
    public path: string
    public key: string
    public type: 'upload' | 'download' | 'compression'
    private _progress: number
    public total: number
    // We will keep track to progress that hasn't budged and ignore it after a while
    private sameProgressCounter: number

    constructor(path: string, key: string, type: 'upload' | 'download' | 'compression') {
        this.path = path;
        this.key = key;
        this.type = type;
        this._progress = 0;
        this.total = -1;
    }

    public get progress(): number {
        return this._progress;
    }

    // We will keep track of non-changing progress so we can eventually treat it as done
    // This is too add resiliency to the extension in case the sever does something wrong
    public set progress(progress: number) {
        if (this._progress == progress) {
            // If this is done uploading, we don't want to forget it early
            if (this._progress < this.total) this.sameProgressCounter++;
        } else {
            this.sameProgressCounter = 0;
            this._progress = progress;
        }
    }

    // We expect the progress number to be set to -1 when it is done
    // This is to avoid timing holes where the extension thinks files are uploaded but the controller is still in the process of uploading them to blob storage
    public isDone = (): boolean => {
        return this.progress < 0 || this.sameProgressCounter > 20;
    }

    // Cancel this progress
    public cancel = async () => {
		const settings = ServerConnection.makeSettings();
		const url = settings.baseUrl + "optumi/cancel-progress";
		const init: RequestInit = {
			method: 'POST',
			body: JSON.stringify({
                key: this.path + this.key,
			}),
		};
		ServerConnection.makeRequest(
			url,
			init, 
			settings
		).then((response: Response) => {
			Global.handleResponse(response);
		});
	}
}

export class FileTracker {
	private polling = false;
    private fileProgress: FileProgress[]

	constructor() {
		this.polling = true;
        this.fileProgress = [];
        // We use an empty request to get all progress that the server knows about
        this.receiveCompressionUpdates(true);
        this.receiveUploadUpdates(true);
        this.receiveDownloadUpdates(true);
	}

    public get = (name: string): FileProgress[] => {
        return [...this.fileProgress.filter(x => x.path == name)]
    }

    public forget = (progress: FileProgress) => {
        this.fileProgress = this.fileProgress.filter(x => x != progress);
    }

    private get compressions() {
        return this.fileProgress.filter(x => x.type == 'compression')
    }

    private get uploads() {
        return this.fileProgress.filter(x => x.type == 'upload')
    }

    private get downloads() {
        return this.fileProgress.filter(x => x.type == 'download')
    }

    public uploadFiles = async (metadata: FileMetadata) => {
        // If there is an unsigned agreement, do not poll
        if (Global.user != null && Global.user.unsignedAgreement) {
            return;
        }

        // If we are already uploading this file, ignore the request
        if (this.compressions.filter(x => x.path == metadata.path).length > 0 || this.uploads.filter(x => x.path == metadata.path).length > 0) return;

        const fileNames = [];
        if (metadata.type == 'directory') {
            for (var file of (await FileServerUtils.getRecursiveTree(metadata.path))) {
                fileNames.push(file);
            }
        } else {
            fileNames.push(metadata.path);
        }

        // Make this unique by adding a timestamp
        const key = new Date().toISOString();

		const settings = ServerConnection.makeSettings();
		const url = settings.baseUrl + "optumi/upload-files";
		const init: RequestInit = {
			method: 'POST',
			body: JSON.stringify({
                key: metadata.path + key,
				fileNames: fileNames,
                compress: Global.user.compressFilesEnabled,
			}),
		};
		ServerConnection.makeRequest(
			url,
			init, 
			settings
		).then((response: Response) => {
			Global.handleResponse(response);
		});
        if (Global.user.compressFilesEnabled) this.fileProgress.push(new FileProgress(metadata.path, key, 'compression'));
        this.fileProgress.push(new FileProgress(metadata.path, key, 'upload'));
        this._filesChanged.emit(void 0);
	}

    public downloadFiles = async (name: string, files: FileMetadata[], workloadUUID: string, moduleUUID: string, overwrite: boolean) => {
        // If there is an unsigned agreement, do not poll
        if (Global.user != null && Global.user.unsignedAgreement) {
            return;
        }

        const fileNames = [];
        const sizes = [];
        for (var file of files) {
            fileNames.push(file.path);
            sizes.push(file.size);
        }
        
        // Make this unique by adding a timestamp
        const key = new Date().toISOString();

		const settings = ServerConnection.makeSettings();
		const url = settings.baseUrl + "optumi/download-files";
		const init: RequestInit = {
			method: 'POST',
			body: JSON.stringify({
				workloadUUID: workloadUUID,
				moduleUUID: moduleUUID,
				key: name + key,
                files: fileNames,
                sizes: sizes,
                overwrite: overwrite,
			}),
		};
		ServerConnection.makeRequest(
			url,
			init, 
			settings
		).then((response: Response) => {
			Global.handleResponse(response);
		});
        this.fileProgress.push(new FileProgress(name, key, 'download'));
        this._filesChanged.emit(void 0);
	}

    private compressionPollDelay = 500;
    private receiveCompressionUpdates = async (empty: boolean = false) => {
        if (!this.polling) return;
        // If there is an unsigned agreement, do not poll
        if (Global.user != null && Global.user.unsignedAgreement) {
            setTimeout(() => this.receiveCompressionUpdates(), this.compressionPollDelay);
            return;
        }

        const fileNames: string[] = [];
        for (var compression of this.compressions) {
            if (!compression.isDone()) fileNames.push(compression.path + compression.key);
        }
        if (fileNames.length > 0 || empty) {
            const settings = ServerConnection.makeSettings();
            const url = settings.baseUrl + "optumi/get-compression-progress";
            const init: RequestInit = {
                method: 'POST',
                body: JSON.stringify({
                    keys: fileNames,
                }),
            };
            ServerConnection.makeRequest(
                url,
                init, 
                settings
            ).then((response: Response) => {
                Global.handleResponse(response);
                setTimeout(() => this.receiveCompressionUpdates(), this.compressionPollDelay);
                if (response.status == 204) {
                    return;
                }
                return response.json();
            }).then((body: any) => {
                if (body) {
                    var changed = false;
                    for (var merged in body) {
                        const path = merged.slice(0, merged.length - 24)
                        const key = merged.slice(merged.length - 24)
                        const progresses = this.compressions.filter(x => x.path == path && x.key == key);
                        var progress;
                        if (progresses.length == 0) {
                            progress = new FileProgress(path, key, 'compression')
                            this.fileProgress.push(progress);
                            // If we are in the process of compressing, we also want to track the upload that will happen after
                            this.fileProgress.push(new FileProgress(path, key, 'upload'));
                        } else {
                            progress = progresses[0];
                        }
                        progress.progress = body[merged].progress;
                        progress.total = body[merged].total;
                        if (progress.isDone()) this.forget(progress);
                        changed = true;
                    }
                    if (changed) this._filesChanged.emit(void 0);
                }
            }, (error: ServerConnection.ResponseError) => {
                setTimeout(() => this.receiveCompressionUpdates(), this.compressionPollDelay);
            });
        } else {
            setTimeout(() => this.receiveCompressionUpdates(), this.compressionPollDelay);
        }
	}

    private uploadPollDelay = 500;
    private receiveUploadUpdates = async (empty: boolean = false) => {
        if (!this.polling) return;
        // If there is an unsigned agreement, do not poll
        if (Global.user != null && Global.user.unsignedAgreement) {
            setTimeout(() => this.receiveUploadUpdates(), this.uploadPollDelay);
            return;
        }

        const fileNames: string[] = [];
        for (var upload of this.uploads) {
            if (!upload.isDone()) fileNames.push(upload.path + upload.key);
        }
        if (fileNames.length > 0 || empty) {
            const settings = ServerConnection.makeSettings();
            const url = settings.baseUrl + "optumi/get-upload-progress";
            const init: RequestInit = {
                method: 'POST',
                body: JSON.stringify({
                    keys: fileNames,
                }),
            };
            ServerConnection.makeRequest(
                url,
                init, 
                settings
            ).then((response: Response) => {
                Global.handleResponse(response);
                setTimeout(() => this.receiveUploadUpdates(), this.uploadPollDelay);
                if (response.status == 204) {
                    return;
                }
                return response.json();
            }).then((body: any) => {
                if (body) {
                    var changed = false;
                    for (var merged in body) {
                        const path = merged.slice(0, merged.length - 24)
                        const key = merged.slice(merged.length - 24)
                        const progresses = this.uploads.filter(x => x.path == path && x.key == key);
                        var progress;
                        if (progresses.length == 0) {
                            progress = new FileProgress(path, key, 'upload')
                            this.fileProgress.push(progress);
                        } else {
                            progress = progresses[0];
                        }
                        progress.progress = body[merged].progress;
                        progress.total = body[merged].total;
                        if (progress.isDone()) this.forget(progress);
                        changed = true;
                    }
                    if (changed) this._filesChanged.emit(void 0);
                }
            }, (error: ServerConnection.ResponseError) => {
                setTimeout(() => this.receiveUploadUpdates(), this.uploadPollDelay);
            });
        } else {
            setTimeout(() => this.receiveUploadUpdates(), this.uploadPollDelay);
        }
	}

    private downloadPollDelay = 500;
    private receiveDownloadUpdates = async (empty: boolean = false) => {
        if (!this.polling) return;
        // If there is an unsigned agreement, do not poll
        if (Global.user != null && Global.user.unsignedAgreement) {
            setTimeout(() => this.receiveDownloadUpdates(), this.downloadPollDelay);
            return;
        }

        const fileNames: string[] = [];
        for (var download of this.downloads) {
            if (!download.isDone()) fileNames.push(download.path + download.key);
        }
        if (fileNames.length > 0 || empty) {
            const settings = ServerConnection.makeSettings();
            const url = settings.baseUrl + "optumi/get-download-progress";
            const init: RequestInit = {
                method: 'POST',
                body: JSON.stringify({
                    keys: fileNames,
                }),
            };
            ServerConnection.makeRequest(
                url,
                init, 
                settings
            ).then((response: Response) => {
                Global.handleResponse(response);
                setTimeout(() => this.receiveDownloadUpdates(), this.downloadPollDelay);
                if (response.status == 204) {
                    return;
                }
                return response.json();
            }).then((body: any) => {
                if (body) {
                    var changed = false;
                    for (var merged in body) {
                        const path = merged.slice(0, merged.length - 24)
                        const key = merged.slice(merged.length - 24)
                        const progresses = this.downloads.filter(x => x.path == path && x.key == key);
                        var progress;
                        if (progresses.length == 0) {
                            progress = new FileProgress(path, key, 'download')
                            this.fileProgress.push(progress);
                        } else {
                            progress = progresses[0];
                        }
                        progress.progress = body[merged].progress;
                        progress.total = body[merged].total;
                        if (progress.isDone()) this.forget(progress);
                        changed = true;
                    }
                    if (changed) this._filesChanged.emit(void 0);
                }
            }, (error: ServerConnection.ResponseError) => {
                setTimeout(() => this.receiveDownloadUpdates(), this.downloadPollDelay);
            });
        } else {
            setTimeout(() => this.receiveDownloadUpdates(), this.downloadPollDelay);
        }
	}

    public stopPolling = () => {
        this.polling = false;
    }

    public getFilesChanged = (): ISignal<this, void> => {
		return this._filesChanged;
	}

    private _filesChanged = new Signal<this, void>(this);
}
