/*
**  Copyright (C) Optumi Inc - All rights reserved.
**
**  You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
**  To receive a copy of the licensing terms please write to contact@optumi.com or visit us at http://www.optumi.com.
**/

import * as React from 'react';
import { Global } from '../../Global';

import { App } from '../../models/application/App';
import { OutputFileEntry } from './OutputFileEntry';

import {
	List,
} from '@material-ui/core';
import { getStyledSwitch } from '../../core/Switch';
import ExtraInfo from '../../utils/ExtraInfo';
import { FileMetadata } from './fileBrowser/FileBrowser';

interface IProps {
	app: App;
}

// Properties for this component
interface IState {
	overwrite: boolean
}

const StyledSwitch = getStyledSwitch();

export class OutputFileList extends React.Component<IProps, IState> {
	_isMounted = false;

	constructor(props: IProps) {
		super(props);
		this.state = {
			overwrite: false
		};
	}

	private getFiles() {
		const files: FileMetadata[] = [];
		for (let module of this.props.app.modules) {
            if (module.files) {
                for (let file of module.files) {
                    files.push(file);
                }
            }
		} 
		if (!this.props.app.running.started) {
			return (
				<div>
					Files will appear here when the job starts.
				</div>
			)
		} else {
			var sorted: FileMetadata[] = files.sort((n1,n2) => {
				if (n1.path > n2.path) {
					return 1;
				}
				if (n1.path < n2.path) {
					return -1;
				}
				return 0;
			});
			const stdout = { path: this.props.app.path.replace('.ipynb', '.stdout'), size: 0 } as FileMetadata;
			const stderr = { path: this.props.app.path.replace('.ipynb', '.stderr'), size: 0 } as FileMetadata;
			return (
				<div>
                    <div style={{display: 'inline-flex', alignItems: 'center'}}>
                        <div style={{paddingLeft: '16px', paddingRight: '16px'}}>
                            <ExtraInfo reminder='Overwrite existing files with downloaded files, or rename the downloaded files'>
								<StyledSwitch
									color='primary'
									inputProps={{style: {height: '24px'}}}
									checked={this.state.overwrite}
									onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
										this.safeSetState({overwrite: event.currentTarget.checked})
									}}
								/>
							</ExtraInfo>
                       </div>
                        Overwrite existing files
                    </div>
                    <List>
						{sorted.map((value: FileMetadata) => 
							React.cloneElement((
								<OutputFileEntry
                                    name={value.path}
                                    files={[value]}
									workloadUUID={this.props.app.uuid}
									moduleUUID={this.props.app.modules[0].uuid}
                                    disabled={false}
                                    overwrite={this.state.overwrite}
								/>
							), { key: value.path })
						)}
                        {this.props.app.interactive && <OutputFileEntry
                            name={'Download stdout as file'}
                            files={[stdout]}
                            workloadUUID={this.props.app.uuid}
                            moduleUUID={this.props.app.modules[0].uuid}
                            disabled={false}
							overwrite={this.state.overwrite}
							
                        />}
                        {this.props.app.interactive && <OutputFileEntry
                            name={'Download stderr as file'}
                            files={[stderr]}
                            workloadUUID={this.props.app.uuid}
                            moduleUUID={this.props.app.modules[0].uuid}
                            disabled={false}
                            overwrite={this.state.overwrite}
                        />}
						<OutputFileEntry
							name={'Download all files'}
							files={sorted.concat([stdout, stderr])}
							workloadUUID={this.props.app.uuid}
							moduleUUID={this.props.app.modules[0].uuid}
							disabled={!this.props.app.interactive && sorted.length == 0}
							overwrite={this.state.overwrite}
						/>
					</List>
				</div>
			)
		}
	}

	public render = (): JSX.Element => {
		if (Global.shouldLogOnRender) console.log('ComponentRender (' + new Date().getSeconds() + ')');
		return (
			<div style={{padding: '12px', width: "100%"}}>
				{this.getFiles()}
			</div>
		);
	}

	// Will be called automatically when the component is mounted
	public componentDidMount = () => {
		this._isMounted = true;
	}

	// Will be called automatically when the component is unmounted
	public componentWillUnmount = () => {
		this._isMounted = false;
	}

	private safeSetState = (map: any) => {
		if (this._isMounted) {
			let update = false
			try {
				for (const key of Object.keys(map)) {
					if (JSON.stringify(map[key]) !== JSON.stringify((this.state as any)[key])) {
						update = true
						break
					}
				}
			} catch (error) {
				update = true
			}
			if (update) {
				if (Global.shouldLogOnSafeSetState) console.log('SafeSetState (' + new Date().getSeconds() + ')');
				this.setState(map)
			} else {
				if (Global.shouldLogOnSafeSetState) console.log('SuppressedSetState (' + new Date().getSeconds() + ')');
			}
		}
	}

	public shouldComponentUpdate = (nextProps: IProps, nextState: IState): boolean => {
        try {
            if (JSON.stringify(this.props) != JSON.stringify(nextProps)) return true;
            if (JSON.stringify(this.state) != JSON.stringify(nextState)) return true;
            if (Global.shouldLogOnRender) console.log('SuppressedRender (' + new Date().getSeconds() + ')');
            return false;
        } catch (error) {
            return true;
        }
    }
}
