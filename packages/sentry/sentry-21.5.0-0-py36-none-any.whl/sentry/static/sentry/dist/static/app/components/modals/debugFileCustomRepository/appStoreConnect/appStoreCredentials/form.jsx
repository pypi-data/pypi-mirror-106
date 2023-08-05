import { __assign, __awaiter, __generator, __makeTemplateObject, __read } from "tslib";
import { Fragment, useState } from 'react';
import styled from '@emotion/styled';
import { addErrorMessage } from 'app/actionCreators/indicator';
import Alert from 'app/components/alert';
import { IconWarning } from 'app/icons';
import { t } from 'app/locale';
import Input from 'app/views/settings/components/forms/controls/input';
import Textarea from 'app/views/settings/components/forms/controls/textarea';
import Field from 'app/views/settings/components/forms/field';
import SelectField from 'app/views/settings/components/forms/selectField';
import Stepper from '../stepper';
import StepActions from '../stepper/stepActions';
var steps = [t('Enter your credentials'), t('Choose an application')];
function Form(_a) {
    var api = _a.api, orgSlug = _a.orgSlug, projectSlug = _a.projectSlug, data = _a.data, onChange = _a.onChange, onCancel = _a.onCancel, onSwitchToReadMode = _a.onSwitchToReadMode;
    var _b = __read(useState(0), 2), activeStep = _b[0], setActiveStep = _b[1];
    var _c = __read(useState(false), 2), isLoading = _c[0], setIsLoading = _c[1];
    var _d = __read(useState([]), 2), appStoreApps = _d[0], setAppStoreApps = _d[1];
    var _e = __read(useState({
        issuer: data.issuer,
        keyId: data.keyId,
        privateKey: data.privateKey,
    }), 2), stepOneData = _e[0], setStepOneData = _e[1];
    var _f = __read(useState({
        app: data.app,
    }), 2), stepTwoData = _f[0], setStepTwoData = _f[1];
    function isFormInvalid() {
        switch (activeStep) {
            case 0:
                return Object.keys(stepOneData).some(function (key) { return !stepOneData[key]; });
            case 1:
                return Object.keys(stepTwoData).some(function (key) { return !stepTwoData[key]; });
            default:
                return false;
        }
    }
    function goNext() {
        setActiveStep(function (prevActiveStep) { return prevActiveStep + 1; });
    }
    function handleGoBack() {
        setActiveStep(function (prevActiveStep) { return prevActiveStep - 1; });
    }
    function handleGoNext() {
        checkAppStoreConnectCredentials();
    }
    function handleSave() {
        var updatedData = __assign(__assign({}, stepOneData), stepTwoData);
        onChange(updatedData);
        onSwitchToReadMode();
    }
    function checkAppStoreConnectCredentials() {
        return __awaiter(this, void 0, void 0, function () {
            var response, _a;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0:
                        setIsLoading(true);
                        _b.label = 1;
                    case 1:
                        _b.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, api.requestPromise("/projects/" + orgSlug + "/" + projectSlug + "/appstoreconnect/apps/", {
                                method: 'POST',
                                data: {
                                    appconnectIssuer: stepOneData.issuer,
                                    appconnectKey: stepOneData.keyId,
                                    appconnectPrivateKey: stepOneData.privateKey,
                                },
                            })];
                    case 2:
                        response = _b.sent();
                        setAppStoreApps(response.apps);
                        setStepTwoData({ app: response.apps[0] });
                        setIsLoading(false);
                        goNext();
                        return [3 /*break*/, 4];
                    case 3:
                        _a = _b.sent();
                        setIsLoading(false);
                        addErrorMessage(t('We could not establish a connection with App Store Connect. Please check the entered App Store Connect credentials.'));
                        return [3 /*break*/, 4];
                    case 4: return [2 /*return*/];
                }
            });
        });
    }
    function renderStepContent(stepIndex) {
        var _a, _b;
        switch (stepIndex) {
            case 0:
                return (<Fragment>
            <Field label={t('Issuer')} inline={false} flexibleControlStateSize stacked required>
              <Input type="text" name="issuer" placeholder={t('Issuer')} value={stepOneData.issuer} onChange={function (e) {
                        return setStepOneData(__assign(__assign({}, stepOneData), { issuer: e.target.value }));
                    }}/>
            </Field>
            <Field label={t('Key ID')} inline={false} flexibleControlStateSize stacked required>
              <Input type="text" name="keyId" placeholder={t('Key Id')} value={stepOneData.keyId} onChange={function (e) {
                        return setStepOneData(__assign(__assign({}, stepOneData), { keyId: e.target.value }));
                    }}/>
            </Field>
            <Field label={t('Private Key')} inline={false} flexibleControlStateSize stacked required>
              <Textarea name="privateKey" placeholder={t('Private Key')} value={stepOneData.privateKey} rows={5} maxRows={5} autosize onChange={function (e) {
                        return setStepOneData(__assign(__assign({}, stepOneData), { privateKey: e.target.value }));
                    }}/>
            </Field>
          </Fragment>);
            case 1:
                return (<StyledSelectField name="application" label={t('App Store Connect Application')} choices={appStoreApps.map(function (appStoreApp) { return [
                        appStoreApp.appId,
                        appStoreApp.name,
                    ]; })} placeholder={t('Select application')} onChange={function (appId) {
                        var selectedAppStoreApp = appStoreApps.find(function (appStoreApp) { return appStoreApp.appId === appId; });
                        setStepTwoData({ app: selectedAppStoreApp });
                    }} value={(_b = (_a = stepTwoData.app) === null || _a === void 0 ? void 0 : _a.appId) !== null && _b !== void 0 ? _b : ''} inline={false} flexibleControlStateSize stacked required/>);
            default:
                return (<Alert type="error" icon={<IconWarning />}>
            {t('This step could not be found.')}
          </Alert>);
        }
    }
    return (<Stepper activeStep={activeStep} steps={steps} renderStepContent={function (index) { return renderStepContent(index); }} renderStepActions={function (index) { return (<StepActions onGoBack={index !== 0 ? handleGoBack : undefined} onGoNext={index !== steps.length - 1 ? handleGoNext : undefined} onCancel={onCancel} onFinish={handleSave} primaryButtonDisabled={isFormInvalid() || isLoading} isLoading={isLoading}/>); }}/>);
}
export default Form;
var StyledSelectField = styled(SelectField)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  padding-right: 0;\n"], ["\n  padding-right: 0;\n"])));
var templateObject_1;
//# sourceMappingURL=form.jsx.map