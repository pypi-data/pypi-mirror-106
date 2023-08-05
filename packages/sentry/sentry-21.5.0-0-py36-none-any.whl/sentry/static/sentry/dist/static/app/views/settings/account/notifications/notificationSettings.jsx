import { __assign, __extends, __read } from "tslib";
import React from 'react';
import AsyncComponent from 'app/components/asyncComponent';
import Avatar from 'app/components/avatar';
import { t } from 'app/locale';
import withOrganizations from 'app/utils/withOrganizations';
import { ACCOUNT_NOTIFICATION_FIELDS } from 'app/views/settings/account/notifications/fields';
import { NOTIFICATION_SETTING_FIELDS } from 'app/views/settings/account/notifications/fields2';
import { backfillMissingProvidersWithFallback, getChoiceString, getFallBackValue, groupByOrganization, isGroupedByProject, providerListToString, } from 'app/views/settings/account/notifications/utils';
import Form from 'app/views/settings/components/forms/form';
import JsonForm from 'app/views/settings/components/forms/jsonForm';
import SettingsPageHeader from 'app/views/settings/components/settingsPageHeader';
import TextBlock from 'app/views/settings/components/text/textBlock';
var NotificationSettings = /** @class */ (function (_super) {
    __extends(NotificationSettings, _super);
    function NotificationSettings() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.getUserDefaultValues = function () {
            var _a;
            /**
             * Get the mapping of providers to values that describe a user's parent-
             * independent notification preferences. The data from the API uses the user
             * ID rather than "me" so we assume the first ID is the user's.
             */
            var notificationType = _this.props.notificationType;
            var notificationSettings = _this.state.notificationSettings;
            return (Object.values(((_a = notificationSettings[notificationType]) === null || _a === void 0 ? void 0 : _a.user) || {}).pop() || {
                email: getFallBackValue(notificationType),
            });
        };
        _this.getParentData = function () {
            return Object.fromEntries(_this.getParents().map(function (parent) { return [
                parent.id,
                Object.values(_this.getParentValues(parent.id))[0],
            ]; }));
        };
        _this.getStateToPutForProvider = function (changedData) {
            var _a, _b;
            /**
             * I don't need to update the provider for EVERY once of the user's projects
             * and organizations, just the user and parents that have explicit settings.
             */
            var notificationType = _this.props.notificationType;
            var notificationSettings = _this.state.notificationSettings;
            var providerList = changedData.provider.split('+');
            var fallbackValue = getFallBackValue(notificationType);
            var updatedNotificationSettings;
            if (Object.keys(notificationSettings).length) {
                updatedNotificationSettings = (_a = {},
                    _a[notificationType] = Object.fromEntries(Object.entries(notificationSettings[notificationType]).map(function (_a) {
                        var _b = __read(_a, 2), scopeType = _b[0], scopeTypeData = _b[1];
                        return [
                            scopeType,
                            Object.fromEntries(Object.entries(scopeTypeData).map(function (_a) {
                                var _b = __read(_a, 2), scopeId = _b[0], scopeIdData = _b[1];
                                return [
                                    scopeId,
                                    backfillMissingProvidersWithFallback(scopeIdData, providerList, fallbackValue),
                                ];
                            })),
                        ];
                    })),
                    _a);
            }
            else {
                // If the user has no settings, we need to create them.
                updatedNotificationSettings = (_b = {},
                    _b[notificationType] = {
                        user: {
                            me: Object.fromEntries(providerList.map(function (provider) { return [provider, fallbackValue]; })),
                        },
                    },
                    _b);
            }
            _this.setState({ notificationSettings: updatedNotificationSettings });
            return updatedNotificationSettings;
        };
        _this.getParentValues = function (parentId) {
            var _a, _b;
            var notificationType = _this.props.notificationType;
            var notificationSettings = _this.state.notificationSettings;
            var parentKey = _this.isGroupedByProject() ? 'project' : 'organization';
            return (((_b = (_a = notificationSettings[notificationType]) === null || _a === void 0 ? void 0 : _a[parentKey]) === null || _b === void 0 ? void 0 : _b[parentId]) || {
                email: 'default',
            });
        };
        _this.getStateToPutForDefault = function (changedData) {
            var _a;
            /** This always updates "user:me". */
            var notificationType = _this.props.notificationType;
            var newValue = Object.values(changedData)[0];
            var previousData = _this.getUserDefaultValues();
            var notificationSettings = (_a = {},
                _a[notificationType] = {
                    user: {
                        me: Object.fromEntries(Object.keys(previousData).map(function (provider) { return [provider, newValue]; })),
                    },
                },
                _a);
            _this.setState({ notificationSettings: notificationSettings });
            return notificationSettings;
        };
        _this.getStateToPutForParent = function (changedData, parentId) {
            var _a, _b, _c;
            /** Get the diff of the Notification Settings for this parent ID. */
            var notificationType = _this.props.notificationType;
            var parentKey = _this.isGroupedByProject() ? 'project' : 'organization';
            var newValue = Object.values(changedData)[0];
            var previousData = _this.getParentValues(parentId);
            var notificationSettings = (_a = {},
                _a[notificationType] = (_b = {},
                    _b[parentKey] = (_c = {},
                        _c[parentId] = Object.fromEntries(Object.entries(previousData).map(function (_a) {
                            var _b = __read(_a, 2), provider = _b[0], _ = _b[1];
                            return [provider, newValue];
                        })),
                        _c),
                    _b),
                _a);
            _this.setState({ notificationSettings: notificationSettings });
            return notificationSettings;
        };
        _this.getGroupedParents = function () {
            /**
             * The UI expects projects to be grouped by organization but can also use
             * this function to make a single group with all organizations.
             */
            var organizations = _this.props.organizations;
            var stateProjects = _this.state.projects;
            return _this.isGroupedByProject()
                ? Object.fromEntries(Object.values(groupByOrganization(stateProjects)).map(function (_a) {
                    var organization = _a.organization, projects = _a.projects;
                    return [organization.name + " Projects", projects];
                }))
                : { organizations: organizations };
        };
        _this.getParentField = function (parent) {
            var _a;
            var _b;
            var notificationType = _this.props.notificationType;
            var defaultFields = NOTIFICATION_SETTING_FIELDS[notificationType];
            var currentDefault = Object.values(_this.getUserDefaultValues())[0];
            return Object.assign({}, defaultFields, {
                label: (<React.Fragment>
          <Avatar {..._a = {}, _a[_this.isGroupedByProject() ? 'project' : 'organization'] = parent, _a}/>
          {parent.slug}
        </React.Fragment>),
                getData: function (data) { return _this.getStateToPutForParent(data, parent.id); },
                name: parent.id,
                choices: (_b = defaultFields.choices) === null || _b === void 0 ? void 0 : _b.concat([
                    [
                        'default',
                        getChoiceString(defaultFields.choices, currentDefault) + " (" + t('default') + ")",
                    ],
                ]),
                defaultValue: 'default',
            });
        };
        _this.getDefaultSettings = function () {
            var notificationType = _this.props.notificationType;
            var title = _this.isGroupedByProject() ? t('All Projects') : t('All Organizations');
            var fields = [
                Object.assign({
                    help: t('This is the default for all projects.'),
                    getData: function (data) { return _this.getStateToPutForDefault(data); },
                }, NOTIFICATION_SETTING_FIELDS[notificationType]),
                Object.assign({
                    help: t('Where personal notifications will be sent.'),
                    getData: function (data) { return _this.getStateToPutForProvider(data); },
                }, NOTIFICATION_SETTING_FIELDS.provider),
            ];
            return [title, fields];
        };
        return _this;
    }
    NotificationSettings.prototype.getDefaultState = function () {
        return __assign(__assign({}, _super.prototype.getDefaultState.call(this)), { notificationSettings: {}, projects: [] });
    };
    NotificationSettings.prototype.getEndpoints = function () {
        var notificationType = this.props.notificationType;
        var query = { type: notificationType };
        var endpoints = [
            ['notificationSettings', "/users/me/notification-settings/", { query: query }],
        ];
        if (this.isGroupedByProject()) {
            endpoints.push(['projects', '/projects/']);
        }
        return endpoints;
    };
    NotificationSettings.prototype.isGroupedByProject = function () {
        /** We can infer the parent type by the `notificationType` key. */
        var notificationType = this.props.notificationType;
        return isGroupedByProject(notificationType);
    };
    NotificationSettings.prototype.getParents = function () {
        /** Use the `notificationType` key to decide which parent objects to use */
        var organizations = this.props.organizations;
        var projects = this.state.projects;
        return this.isGroupedByProject() ? projects : organizations;
    };
    NotificationSettings.prototype.renderBody = function () {
        var _a;
        var _this = this;
        var notificationType = this.props.notificationType;
        var _b = ACCOUNT_NOTIFICATION_FIELDS[notificationType], title = _b.title, description = _b.description;
        var groupedParents = this.getGroupedParents();
        var userData = this.getUserDefaultValues();
        var parentData = this.getParentData();
        var _c = __read(this.getDefaultSettings(), 2), formTitle = _c[0], fields = _c[1];
        return (<React.Fragment>
        <SettingsPageHeader title={title}/>
        {description && <TextBlock>{description}</TextBlock>}
        <Form saveOnBlur apiMethod="PUT" apiEndpoint="/users/me/notification-settings/" initialData={_a = {},
                _a[notificationType] = Object.values(userData)[0],
                _a.provider = providerListToString(Object.keys(userData)),
                _a}>
          <JsonForm title={formTitle} fields={fields}/>
        </Form>
        <Form saveOnBlur apiMethod="PUT" apiEndpoint="/users/me/notification-settings/" initialData={parentData}>
          {Object.entries(groupedParents).map(function (_a) {
                var _b = __read(_a, 2), groupTitle = _b[0], parents = _b[1];
                return (<JsonForm key={groupTitle} title={groupTitle} fields={parents.map(function (parent) { return _this.getParentField(parent); })}/>);
            })}
        </Form>
      </React.Fragment>);
    };
    return NotificationSettings;
}(AsyncComponent));
export default withOrganizations(NotificationSettings);
//# sourceMappingURL=notificationSettings.jsx.map