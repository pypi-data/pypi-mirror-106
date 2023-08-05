import { useContext } from 'react';
import withProject from 'app/utils/withProject';
import SettingsNavigation from 'app/views/settings/components/settingsNavigation';
import getConfiguration from 'app/views/settings/project/navigationConfiguration';
import AppStoreConnectContext from './appStoreConnectContext';
var ProjectSettingsNavigation = function (_a) {
    var organization = _a.organization, project = _a.project;
    var appStoreConnectContext = useContext(AppStoreConnectContext);
    var debugFilesNeedsReview = appStoreConnectContext
        ? Object.keys(appStoreConnectContext !== null && appStoreConnectContext !== void 0 ? appStoreConnectContext : {}).some(function (key) { return !appStoreConnectContext[key]; })
        : false;
    return (<SettingsNavigation navigationObjects={getConfiguration({ project: project, organization: organization, debugFilesNeedsReview: debugFilesNeedsReview })} access={new Set(organization.access)} features={new Set(organization.features)} organization={organization} project={project}/>);
};
export default withProject(ProjectSettingsNavigation);
//# sourceMappingURL=projectSettingsNavigation.jsx.map