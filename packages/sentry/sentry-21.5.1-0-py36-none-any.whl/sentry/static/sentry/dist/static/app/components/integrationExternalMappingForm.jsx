import { __assign, __extends } from "tslib";
import { Component } from 'react';
import capitalize from 'lodash/capitalize';
import pick from 'lodash/pick';
import { t, tct } from 'app/locale';
import { FieldFromConfig } from 'app/views/settings/components/forms';
import Form from 'app/views/settings/components/forms/form';
var IntegrationExternalMappingForm = /** @class */ (function (_super) {
    __extends(IntegrationExternalMappingForm, _super);
    function IntegrationExternalMappingForm() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(IntegrationExternalMappingForm.prototype, "initialData", {
        get: function () {
            var _a = this.props, integration = _a.integration, mapping = _a.mapping;
            return __assign({ externalName: '', userId: '', teamId: '', sentryName: '', provider: integration.provider.key, integrationId: integration.id }, pick(mapping, ['externalName', 'userId', 'sentryName', 'teamId']));
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(IntegrationExternalMappingForm.prototype, "formFields", {
        get: function () {
            var _a = this.props, sentryNames = _a.sentryNames, type = _a.type;
            var options = sentryNames.map(function (_a) {
                var name = _a.name, id = _a.id;
                return ({ value: id, label: name });
            });
            var fields = [
                {
                    name: 'externalName',
                    type: 'string',
                    required: true,
                    label: tct('External [type]', { type: capitalize(type) }),
                    placeholder: t("" + (type === 'team' ? '@org/teamname' : '@username')),
                },
            ];
            if (type === 'user') {
                fields.push({
                    name: 'userId',
                    type: 'select',
                    required: true,
                    label: tct('Sentry [type]', { type: capitalize(type) }),
                    placeholder: t("Choose your Sentry User"),
                    options: options,
                });
            }
            if (type === 'team') {
                fields.push({
                    name: 'teamId',
                    type: 'select',
                    required: true,
                    label: tct('Sentry [type]', { type: capitalize(type) }),
                    placeholder: t("Choose your Sentry Team"),
                    options: options,
                });
            }
            return fields;
        },
        enumerable: false,
        configurable: true
    });
    IntegrationExternalMappingForm.prototype.render = function () {
        var _a = this.props, onSubmitSuccess = _a.onSubmitSuccess, onCancel = _a.onCancel, mapping = _a.mapping, baseEndpoint = _a.baseEndpoint, onSubmit = _a.onSubmit;
        // endpoint changes if we are making a new row or updating an existing one
        var endpoint = !baseEndpoint
            ? undefined
            : mapping
                ? "" + baseEndpoint + mapping.id + "/"
                : baseEndpoint;
        var apiMethod = !baseEndpoint ? undefined : mapping ? 'PUT' : 'POST';
        return (<Form onSubmitSuccess={onSubmitSuccess} initialData={this.initialData} apiEndpoint={endpoint} apiMethod={apiMethod} onCancel={onCancel} onSubmit={onSubmit}>
        {this.formFields.map(function (field) { return (<FieldFromConfig key={field.name} field={field} inline={false} stacked flexibleControlStateSize/>); })}
      </Form>);
    };
    return IntegrationExternalMappingForm;
}(Component));
export default IntegrationExternalMappingForm;
//# sourceMappingURL=integrationExternalMappingForm.jsx.map