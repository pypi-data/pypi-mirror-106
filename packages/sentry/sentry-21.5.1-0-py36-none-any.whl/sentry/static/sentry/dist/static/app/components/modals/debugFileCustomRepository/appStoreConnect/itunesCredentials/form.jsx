import { __assign, __awaiter, __generator, __makeTemplateObject, __read } from "tslib";
import { Fragment, useState } from 'react';
import styled from '@emotion/styled';
import { addErrorMessage } from 'app/actionCreators/indicator';
import Alert from 'app/components/alert';
import Button from 'app/components/button';
import ButtonBar from 'app/components/buttonBar';
import { IconInfo, IconMobile, IconRefresh, IconWarning } from 'app/icons';
import { t } from 'app/locale';
import space from 'app/styles/space';
import Input from 'app/views/settings/components/forms/controls/input';
import Field from 'app/views/settings/components/forms/field';
import SelectField from 'app/views/settings/components/forms/selectField';
import Stepper from '../stepper';
import StepActions from '../stepper/stepActions';
var steps = [
    t('Enter your credentials'),
    t('Enter your authentication code'),
    t('Choose an organization'),
];
function Form(_a) {
    var api = _a.api, orgSlug = _a.orgSlug, projectSlug = _a.projectSlug, data = _a.data, onChange = _a.onChange, onSwitchToReadMode = _a.onSwitchToReadMode, onCancel = _a.onCancel;
    var _b = __read(useState(0), 2), activeStep = _b[0], setActiveStep = _b[1];
    var _c = __read(useState(false), 2), isLoading = _c[0], setIsLoading = _c[1];
    var _d = __read(useState(''), 2), sessionContext = _d[0], setSessionContext = _d[1];
    var _e = __read(useState(false), 2), useSms = _e[0], setUseSms = _e[1];
    var _f = __read(useState([]), 2), appStoreOrgs = _f[0], setAppStoreOrgs = _f[1];
    var _g = __read(useState({
        username: data.username,
        password: data.password,
    }), 2), stepOneData = _g[0], setSetpOneData = _g[1];
    var _h = __read(useState({
        authenticationCode: data.authenticationCode,
    }), 2), stepTwoData = _h[0], setStepTwoData = _h[1];
    var _j = __read(useState({
        org: data.org,
    }), 2), stepThreeData = _j[0], setStepThreeData = _j[1];
    function isFormInvalid() {
        switch (activeStep) {
            case 0:
                return Object.keys(stepOneData).some(function (key) { return !stepOneData[key]; });
            case 1:
                return Object.keys(stepTwoData).some(function (key) { return !stepTwoData[key]; });
            case 2:
                return Object.keys(stepThreeData).some(function (key) { return !stepThreeData[key]; });
            default:
                return false;
        }
    }
    function goNext() {
        setActiveStep(function (prevActiveStep) { return prevActiveStep + 1; });
    }
    function handleGoBack() {
        var newActiveStep = activeStep - 1;
        switch (newActiveStep) {
            case 1:
                startItunesAuthentication(false);
                setStepTwoData({ authenticationCode: undefined });
                break;
            default:
                break;
        }
        setActiveStep(newActiveStep);
    }
    function handleGoNext() {
        switch (activeStep) {
            case 0:
                startItunesAuthentication();
                break;
            case 1:
                startTwoFactorAuthentication();
                break;
            default:
                break;
        }
    }
    function handleSave() {
        onChange(__assign(__assign(__assign(__assign({}, stepOneData), stepTwoData), stepThreeData), { sessionContext: sessionContext, useSms: useSms }));
        onSwitchToReadMode();
    }
    function startItunesAuthentication(shouldGoNext) {
        if (shouldGoNext === void 0) { shouldGoNext = true; }
        return __awaiter(this, void 0, void 0, function () {
            var response, _a;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0:
                        if (shouldGoNext) {
                            setIsLoading(true);
                        }
                        if (useSms) {
                            setUseSms(false);
                        }
                        _b.label = 1;
                    case 1:
                        _b.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, api.requestPromise("/projects/" + orgSlug + "/" + projectSlug + "/appstoreconnect/start/", {
                                method: 'POST',
                                data: {
                                    itunesUser: stepOneData.username,
                                    itunesPassword: stepOneData.password,
                                },
                            })];
                    case 2:
                        response = _b.sent();
                        setSessionContext(response.sessionContext);
                        if (shouldGoNext) {
                            setIsLoading(false);
                            goNext();
                        }
                        return [3 /*break*/, 4];
                    case 3:
                        _a = _b.sent();
                        if (shouldGoNext) {
                            setIsLoading(false);
                        }
                        addErrorMessage(t('The iTunes authentication failed. Please check the entered credentials.'));
                        return [3 /*break*/, 4];
                    case 4: return [2 /*return*/];
                }
            });
        });
    }
    function startTwoFactorAuthentication() {
        return __awaiter(this, void 0, void 0, function () {
            var response, organizations, newSessionContext, _a;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0:
                        setIsLoading(true);
                        _b.label = 1;
                    case 1:
                        _b.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, api.requestPromise("/projects/" + orgSlug + "/" + projectSlug + "/appstoreconnect/2fa/", {
                                method: 'POST',
                                data: {
                                    code: stepTwoData.authenticationCode,
                                    useSms: useSms,
                                    sessionContext: sessionContext,
                                },
                            })];
                    case 2:
                        response = _b.sent();
                        setIsLoading(false);
                        organizations = response.organizations, newSessionContext = response.sessionContext;
                        setStepThreeData({ org: organizations[0] });
                        setAppStoreOrgs(organizations);
                        setSessionContext(newSessionContext);
                        goNext();
                        return [3 /*break*/, 4];
                    case 3:
                        _a = _b.sent();
                        setIsLoading(false);
                        addErrorMessage(t('The two factor authentication failed. Please check the entered code.'));
                        return [3 /*break*/, 4];
                    case 4: return [2 /*return*/];
                }
            });
        });
    }
    function startSmsAuthentication() {
        return __awaiter(this, void 0, void 0, function () {
            var response, _a;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0:
                        if (!useSms) {
                            setUseSms(true);
                        }
                        _b.label = 1;
                    case 1:
                        _b.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, api.requestPromise("/projects/" + orgSlug + "/" + projectSlug + "/appstoreconnect/requestSms/", {
                                method: 'POST',
                                data: { sessionContext: sessionContext },
                            })];
                    case 2:
                        response = _b.sent();
                        setSessionContext(response.sessionContext);
                        return [3 /*break*/, 4];
                    case 3:
                        _a = _b.sent();
                        addErrorMessage(t('An error occured while sending the SMS. Please try again'));
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
            <Field label={t('Username')} inline={false} flexibleControlStateSize stacked required>
              <Input type="text" name="username" placeholder={t('Username')} onChange={function (e) { return setSetpOneData(__assign(__assign({}, stepOneData), { username: e.target.value })); }}/>
            </Field>
            <Field label={t('Password')} inline={false} flexibleControlStateSize stacked required>
              <Input type="password" name="password" placeholder={t('Password')} onChange={function (e) { return setSetpOneData(__assign(__assign({}, stepOneData), { password: e.target.value })); }}/>
            </Field>
          </Fragment>);
            case 1:
                return (<Fragment>
            <StyledAlert type="info" icon={<IconInfo />}>
              <AlertContent>
                {t('Did not get a verification code?')}
                <ButtonBar gap={1}>
                  <Button size="small" title={t('Get a new verification code')} onClick={function () { return startItunesAuthentication(false); }} icon={<IconRefresh />}>
                    {t('Resend code')}
                  </Button>
                  <Button size="small" title={t('Get a text message with a code')} onClick={function () { return startSmsAuthentication(); }} icon={<IconMobile />}>
                    {t('Text me')}
                  </Button>
                </ButtonBar>
              </AlertContent>
            </StyledAlert>
            <Field label={t('Two Factor authentication code')} inline={false} flexibleControlStateSize stacked required>
              <Input type="text" name="two-factor-authentication-code" placeholder={t('Enter your code')} value={stepTwoData.authenticationCode} onChange={function (e) {
                        return setStepTwoData(__assign(__assign({}, setStepTwoData), { authenticationCode: e.target.value }));
                    }}/>
            </Field>
          </Fragment>);
            case 2:
                return (<StyledSelectField name="organization" label={t('iTunes Organization')} choices={appStoreOrgs.map(function (appStoreOrg) { return [
                        appStoreOrg.organizationId,
                        appStoreOrg.name,
                    ]; })} placeholder={t('Select organization')} onChange={function (organizationId) {
                        var selectedAppStoreOrg = appStoreOrgs.find(function (appStoreOrg) { return appStoreOrg.organizationId === organizationId; });
                        setStepThreeData({ org: selectedAppStoreOrg });
                    }} value={(_b = (_a = stepThreeData.org) === null || _a === void 0 ? void 0 : _a.organizationId) !== null && _b !== void 0 ? _b : ''} inline={false} flexibleControlStateSize stacked required/>);
            default:
                return (<Alert type="error" icon={<IconWarning />}>
            {t('This step could not be found.')}
          </Alert>);
        }
    }
    return (<Stepper activeStep={activeStep} steps={steps} renderStepContent={function (index) { return renderStepContent(index); }} renderStepActions={function (index) { return (<StepActions onGoBack={index !== 0 ? handleGoBack : undefined} onGoNext={index !== steps.length - 1 ? handleGoNext : undefined} onCancel={onCancel} onFinish={handleSave} primaryButtonDisabled={isFormInvalid() || isLoading} isLoading={isLoading}/>); }}/>);
}
export default Form;
var StyledAlert = styled(Alert)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: grid;\n  grid-template-columns: max-content 1fr;\n  align-items: center;\n"], ["\n  display: grid;\n  grid-template-columns: max-content 1fr;\n  align-items: center;\n"])));
var AlertContent = styled('div')(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: grid;\n  grid-template-columns: 1fr max-content;\n  align-items: center;\n  grid-gap: ", ";\n"], ["\n  display: grid;\n  grid-template-columns: 1fr max-content;\n  align-items: center;\n  grid-gap: ", ";\n"])), space(2));
var StyledSelectField = styled(SelectField)(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  padding-right: 0;\n"], ["\n  padding-right: 0;\n"])));
var templateObject_1, templateObject_2, templateObject_3;
//# sourceMappingURL=form.jsx.map