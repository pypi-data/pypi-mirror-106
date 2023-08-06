import { __assign, __extends, __makeTemplateObject, __read } from "tslib";
import React from 'react';
import styled from '@emotion/styled';
import Alert from 'app/components/alert';
import AsyncComponent from 'app/components/asyncComponent';
import Avatar from 'app/components/avatar';
import { IconInfo } from 'app/icons';
import { t, tct } from 'app/locale';
import space from 'app/styles/space';
import withOrganizations from 'app/utils/withOrganizations';
import { ACCOUNT_NOTIFICATION_FIELDS } from 'app/views/settings/account/notifications/fields';
import { NOTIFICATION_SETTING_FIELDS } from 'app/views/settings/account/notifications/fields2';
import { backfillMissingProvidersWithFallback, getChoiceString, getFallBackValue, groupByOrganization, isGroupedByProject, mergeNotificationSettings, providerListToString, } from 'app/views/settings/account/notifications/utils';
import Form from 'app/views/settings/components/forms/form';
import JsonForm from 'app/views/settings/components/forms/jsonForm';
import SettingsPageHeader from 'app/views/settings/components/settingsPageHeader';
import TextBlock from 'app/views/settings/components/text/textBlock';
var NotificationSettings = /** @class */ (function (_super) {
    __extends(NotificationSettings, _super);
    function NotificationSettings() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.getParentKey = function () {
            return _this.isGroupedByProject() ? 'project' : 'organization';
        };
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
        _this.getParentValues = function (parentId) {
            var _a, _b;
            var notificationType = _this.props.notificationType;
            var notificationSettings = _this.state.notificationSettings;
            return (((_b = (_a = notificationSettings[notificationType]) === null || _a === void 0 ? void 0 : _a[_this.getParentKey()]) === null || _b === void 0 ? void 0 : _b[parentId]) || {
                email: 'default',
            });
        };
        _this.getParentData = function () {
            /** Get a mapping of all parent IDs to the notification setting for the current providers. */
            var provider = _this.getCurrentProviders()[0];
            return Object.fromEntries(_this.getParents().map(function (parent) { return [
                parent.id,
                _this.getParentValues(parent.id)[provider],
            ]; }));
        };
        _this.getCurrentProviders = function () {
            /** Get the list of providers currently active on this page. Note: this can be empty. */
            var userData = _this.getUserDefaultValues();
            return Object.entries(userData)
                .filter(function (_a) {
                var _b = __read(_a, 2), _ = _b[0], value = _b[1];
                return !['never'].includes(value);
            })
                .map(function (_a) {
                var _b = __read(_a, 2), provider = _b[0], _ = _b[1];
                return provider;
            });
        };
        /* Methods responsible for updating state and hitting the API. */
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
                                    backfillMissingProvidersWithFallback(scopeIdData, providerList, fallbackValue, scopeType),
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
            _this.setState({
                notificationSettings: mergeNotificationSettings(notificationSettings, updatedNotificationSettings),
            });
            return updatedNotificationSettings;
        };
        _this.getStateToPutForDefault = function (changedData) {
            var _a;
            /**
             * Update the current providers' parent-independent notification settings
             * with the new value. If the new value is "never", then also update all
             * parent-specific notification settings to "default". If the previous value
             * was "never", then assume providerList should be "email" only.
             */
            var notificationType = _this.props.notificationType;
            var notificationSettings = _this.state.notificationSettings;
            var newValue = Object.values(changedData)[0];
            var providerList = _this.getCurrentProviders();
            if (!providerList.length) {
                providerList = ['email'];
            }
            var updatedNotificationSettings = (_a = {},
                _a[notificationType] = {
                    user: {
                        me: Object.fromEntries(providerList.map(function (provider) { return [provider, newValue]; })),
                    },
                },
                _a);
            if (newValue === 'never') {
                updatedNotificationSettings[notificationType][_this.getParentKey()] = Object.fromEntries(_this.getParents().map(function (parent) { return [
                    parent.id,
                    Object.fromEntries(providerList.map(function (provider) { return [provider, 'default']; })),
                ]; }));
            }
            _this.setState({
                notificationSettings: mergeNotificationSettings(notificationSettings, updatedNotificationSettings),
            });
            return updatedNotificationSettings;
        };
        _this.getStateToPutForParent = function (changedData, parentId) {
            var _a, _b, _c;
            /** Get the diff of the Notification Settings for this parent ID. */
            var notificationType = _this.props.notificationType;
            var notificationSettings = _this.state.notificationSettings;
            var currentProviders = _this.getCurrentProviders();
            var newValue = Object.values(changedData)[0];
            var updatedNotificationSettings = (_a = {},
                _a[notificationType] = (_b = {},
                    _b[_this.getParentKey()] = (_c = {},
                        _c[parentId] = Object.fromEntries(currentProviders.map(function (provider) { return [provider, newValue]; })),
                        _c),
                    _b),
                _a);
            _this.setState({
                notificationSettings: mergeNotificationSettings(notificationSettings, updatedNotificationSettings),
            });
            return updatedNotificationSettings;
        };
        /* Methods responsible for rendering the page. */
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
                label: (<FieldLabel>
          <Avatar {..._a = {}, _a[_this.isGroupedByProject() ? 'project' : 'organization'] = parent, _a}/>
          <span>{parent.slug}</span>
        </FieldLabel>),
                getData: function (data) { return _this.getStateToPutForParent(data, parent.id); },
                name: parent.id,
                choices: (_b = defaultFields.choices) === null || _b === void 0 ? void 0 : _b.concat([
                    [
                        'default',
                        t('Default') + " (" + getChoiceString(defaultFields.choices, currentDefault) + ")",
                    ],
                ]),
                defaultValue: 'default',
            });
        };
        _this.isEverythingDisabled = function () {
            var _a;
            /**
             * For a given notificationType, are the parent-independent setting "never"
             * for all providers and are the parent-specific settings "default" or
             * "never". If so, the API is telling us that the user has opted out of
             * all notifications.
             */
            var notificationType = _this.props.notificationType;
            var notificationSettings = _this.state.notificationSettings;
            return (
            // For user, all providers are "never".
            Object.values(_this.getUserDefaultValues()).every(function (value) { return value === 'never'; }) &&
                // Every leaf value is either "never" or "default".
                Object.values(((_a = notificationSettings[notificationType]) === null || _a === void 0 ? void 0 : _a[_this.getParentKey()]) || {}).every(function (settingsByProvider) {
                    return Object.values(settingsByProvider).every(function (value) {
                        return ['never', 'default'].includes(value);
                    });
                }));
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
    /* Helper methods that help interpret state. */
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
    NotificationSettings.prototype.getInitialData = function () {
        var _a;
        var notificationType = this.props.notificationType;
        var providerList = this.getCurrentProviders();
        var initialData = (_a = {},
            _a[notificationType] = providerList.length
                ? this.getUserDefaultValues()[providerList[0]]
                : 'never',
            _a);
        if (!this.isEverythingDisabled()) {
            initialData.provider = providerListToString(providerList);
        }
        return initialData;
    };
    NotificationSettings.prototype.getFields = function () {
        var _this = this;
        var notificationType = this.props.notificationType;
        var fields = [
            Object.assign({
                help: t('This is the default for all projects.'),
                getData: function (data) { return _this.getStateToPutForDefault(data); },
            }, NOTIFICATION_SETTING_FIELDS[notificationType]),
        ];
        if (!this.isEverythingDisabled()) {
            fields.push(Object.assign({
                help: t('Where personal notifications will be sent.'),
                getData: function (data) { return _this.getStateToPutForProvider(data); },
            }, NOTIFICATION_SETTING_FIELDS.provider));
        }
        return fields;
    };
    NotificationSettings.prototype.renderBody = function () {
        var _this = this;
        var notificationType = this.props.notificationType;
        var _a = ACCOUNT_NOTIFICATION_FIELDS[notificationType], title = _a.title, description = _a.description;
        return (<React.Fragment>
        <SettingsPageHeader title={title}/>
        {description && <TextBlock>{description}</TextBlock>}
        <FeedbackAlert type="info" icon={<IconInfo />}>
          {tct('Got feedback? Email [email:ecosystem-feedback@sentry.io].', {
                email: <a href="mailto:ecosystem-feedback@sentry.io"/>,
            })}
        </FeedbackAlert>
        <Form saveOnBlur apiMethod="PUT" apiEndpoint="/users/me/notification-settings/" initialData={this.getInitialData()}>
          <JsonForm title={this.isGroupedByProject() ? t('All Projects') : t('All Organizations')} fields={this.getFields()}/>
        </Form>
        {!this.isEverythingDisabled() && (<Form saveOnBlur apiMethod="PUT" apiEndpoint="/users/me/notification-settings/" initialData={this.getParentData()}>
            {Object.entries(this.getGroupedParents()).map(function (_a) {
                    var _b = __read(_a, 2), groupTitle = _b[0], parents = _b[1];
                    return (<JsonForm key={groupTitle} title={groupTitle} fields={parents.map(function (parent) { return _this.getParentField(parent); })}/>);
                })}
          </Form>)}
      </React.Fragment>);
    };
    return NotificationSettings;
}(AsyncComponent));
var FieldLabel = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: flex;\n  gap: ", ";\n  line-height: 16px;\n"], ["\n  display: flex;\n  gap: ", ";\n  line-height: 16px;\n"])), space(0.5));
var FeedbackAlert = styled(Alert)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  margin: 20px 0px;\n"], ["\n  margin: 20px 0px;\n"])));
export default withOrganizations(NotificationSettings);
var templateObject_1, templateObject_2;
//# sourceMappingURL=notificationSettings.jsx.map