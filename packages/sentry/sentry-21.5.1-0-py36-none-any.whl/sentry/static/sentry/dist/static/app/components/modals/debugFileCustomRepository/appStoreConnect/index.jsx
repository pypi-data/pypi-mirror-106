import { __awaiter, __generator, __makeTemplateObject, __read } from "tslib";
import { Fragment, useContext, useState } from 'react';
import styled from '@emotion/styled';
import isEqual from 'lodash/isEqual';
import { addErrorMessage, addSuccessMessage } from 'app/actionCreators/indicator';
import Alert from 'app/components/alert';
import Button from 'app/components/button';
import ButtonBar from 'app/components/buttonBar';
import List from 'app/components/list';
import ListItem from 'app/components/list/listItem';
import { Panel } from 'app/components/panels';
import { IconWarning } from 'app/icons';
import { t } from 'app/locale';
import space from 'app/styles/space';
import withApi from 'app/utils/withApi';
import AppStoreConnectContext from 'app/views/settings/project/appStoreConnectContext';
import AppStoreCredentials from './appStoreCredentials';
import ItunesCredentials from './itunesCredentials';
function AppStoreConnect(_a) {
    var Body = _a.Body, Footer = _a.Footer, closeModal = _a.closeModal, api = _a.api, initialData = _a.initialData, orgSlug = _a.orgSlug, projectSlug = _a.projectSlug, onSubmit = _a.onSubmit;
    var appStoreConnenctContext = useContext(AppStoreConnectContext);
    var _b = __read(useState(false), 2), isLoading = _b[0], setIsLoading = _b[1];
    var appStoreCredentialsInitialData = {
        issuer: initialData === null || initialData === void 0 ? void 0 : initialData.appconnectIssuer,
        keyId: initialData === null || initialData === void 0 ? void 0 : initialData.appconnectKey,
        privateKey: undefined,
        app: (initialData === null || initialData === void 0 ? void 0 : initialData.appName) && (initialData === null || initialData === void 0 ? void 0 : initialData.appId)
            ? {
                appId: initialData.appId,
                name: initialData.appName,
            }
            : undefined,
    };
    var iTunesCredentialsInitialData = {
        username: initialData === null || initialData === void 0 ? void 0 : initialData.itunesUser,
        password: undefined,
        authenticationCode: undefined,
        org: (initialData === null || initialData === void 0 ? void 0 : initialData.orgId) && (initialData === null || initialData === void 0 ? void 0 : initialData.orgName)
            ? {
                organizationId: initialData.orgId,
                name: initialData.appName,
            }
            : undefined,
        useSms: undefined,
        sessionContext: undefined,
    };
    var _c = __read(useState(appStoreCredentialsInitialData), 2), appStoreCredentialsData = _c[0], setAppStoreCredentialsData = _c[1];
    var _d = __read(useState(iTunesCredentialsInitialData), 2), iTunesCredentialsData = _d[0], setItunesCredentialsData = _d[1];
    function handleSave() {
        var _a, _b, _c, _d;
        return __awaiter(this, void 0, void 0, function () {
            var endpoint, successMessage, errorMessage, response, _e;
            return __generator(this, function (_f) {
                switch (_f.label) {
                    case 0:
                        endpoint = "/projects/" + orgSlug + "/" + projectSlug + "/appstoreconnect/";
                        successMessage = t('App Store Connect repository was successfully added');
                        errorMessage = t('An error occured while adding the App Store Connect repository');
                        if (!!initialData) {
                            endpoint = "" + endpoint + initialData.id + "/";
                            successMessage = t('App Store Connect repository was successfully updated');
                            errorMessage = t('An error occured while updating the App Store Connect repository');
                        }
                        setIsLoading(true);
                        _f.label = 1;
                    case 1:
                        _f.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, api.requestPromise(endpoint, {
                                method: 'POST',
                                data: {
                                    appconnectIssuer: appStoreCredentialsData.issuer,
                                    appconnectKey: appStoreCredentialsData.keyId,
                                    appconnectPrivateKey: appStoreCredentialsData.privateKey,
                                    appName: (_a = appStoreCredentialsData.app) === null || _a === void 0 ? void 0 : _a.name,
                                    appId: (_b = appStoreCredentialsData.app) === null || _b === void 0 ? void 0 : _b.appId,
                                    itunesUser: iTunesCredentialsData.username,
                                    itunesPassword: iTunesCredentialsData.password,
                                    orgId: (_c = iTunesCredentialsData.org) === null || _c === void 0 ? void 0 : _c.organizationId,
                                    orgName: (_d = iTunesCredentialsData.org) === null || _d === void 0 ? void 0 : _d.name,
                                    sessionContext: iTunesCredentialsData.sessionContext,
                                },
                            })];
                    case 2:
                        response = _f.sent();
                        addSuccessMessage(successMessage);
                        setIsLoading(false);
                        onSubmit(response);
                        closeModal();
                        return [3 /*break*/, 4];
                    case 3:
                        _e = _f.sent();
                        setIsLoading(false);
                        addErrorMessage(errorMessage);
                        return [3 /*break*/, 4];
                    case 4: return [2 /*return*/];
                }
            });
        });
    }
    var isUpdating = !!initialData;
    function isDataInvalid(data) {
        return Object.keys(data).some(function (key) {
            var value = data[key];
            if (typeof value === 'string') {
                return !value.trim();
            }
            return typeof value === 'undefined';
        });
    }
    function isAppStoreCredentialsDataInvalid() {
        return isDataInvalid(appStoreCredentialsData);
    }
    function isItunesCredentialsDataInvalid() {
        return isDataInvalid(iTunesCredentialsData);
    }
    function isFormInvalid() {
        if (!!initialData) {
            var isAppStoreCredentialsDataTheSame = isEqual(appStoreCredentialsData, appStoreCredentialsInitialData);
            var isItunesCredentialsDataTheSame = isEqual(iTunesCredentialsData, iTunesCredentialsInitialData);
            if (!isAppStoreCredentialsDataTheSame && !isItunesCredentialsDataTheSame) {
                return isAppStoreCredentialsDataInvalid() && isItunesCredentialsDataInvalid();
            }
            if (!isAppStoreCredentialsDataTheSame) {
                return isAppStoreCredentialsDataInvalid();
            }
            if (!isItunesCredentialsDataTheSame) {
                return isItunesCredentialsDataInvalid();
            }
            return isAppStoreCredentialsDataTheSame && isItunesCredentialsDataTheSame;
        }
        return isAppStoreCredentialsDataInvalid() && isItunesCredentialsDataInvalid();
    }
    return (<Fragment>
      <Body>
        <StyledList symbol="colored-numeric">
          <ListItem>
            <ItemTitle>{t('App Store Connect credentials')}</ItemTitle>
            {!!(appStoreConnenctContext === null || appStoreConnenctContext === void 0 ? void 0 : appStoreConnenctContext.appstoreCredentialsValid) && (<StyledAlert type="warning" icon={<IconWarning />}>
                {t('Your App Store Connect credentials are invalid. To reconnect, update your credentials')}
              </StyledAlert>)}
            <ItemContent>
              <AppStoreCredentials api={api} orgSlug={orgSlug} projectSlug={projectSlug} data={appStoreCredentialsData} onChange={setAppStoreCredentialsData} onReset={function () { return setAppStoreCredentialsData(appStoreCredentialsInitialData); }} isUpdating={isUpdating}/>
            </ItemContent>
          </ListItem>
          <ListItem>
            <ItemTitle>{t('iTunes credentials')}</ItemTitle>
            {!!(appStoreConnenctContext === null || appStoreConnenctContext === void 0 ? void 0 : appStoreConnenctContext.itunesSessionValid) && (<StyledAlert type="warning" icon={<IconWarning />}>
                {t('Your iTunes session has expired. To reconnect, sign in with your Apple ID and password')}
              </StyledAlert>)}
            <ItemContent>
              <ItunesCredentials api={api} orgSlug={orgSlug} projectSlug={projectSlug} data={iTunesCredentialsData} onChange={setItunesCredentialsData} onReset={function () { return setItunesCredentialsData(iTunesCredentialsInitialData); }} isUpdating={isUpdating}/>
            </ItemContent>
          </ListItem>
        </StyledList>
      </Body>
      <Footer>
        <ButtonBar gap={1.5}>
          <Button onClick={closeModal}>{t('Cancel')}</Button>
          <StyledButton priority="primary" onClick={handleSave} disabled={isFormInvalid() || isLoading}>
            {t('Save')}
          </StyledButton>
        </ButtonBar>
      </Footer>
    </Fragment>);
}
export default withApi(AppStoreConnect);
var StyledList = styled(List)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  grid-gap: 0;\n  & > li {\n    padding-left: 0;\n    display: grid;\n    grid-gap: ", ";\n  }\n"], ["\n  grid-gap: 0;\n  & > li {\n    padding-left: 0;\n    display: grid;\n    grid-gap: ", ";\n  }\n"])), space(1));
var ItemTitle = styled('div')(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  padding-left: ", ";\n  margin-bottom: ", ";\n"], ["\n  padding-left: ", ";\n  margin-bottom: ", ";\n"])), space(4), space(1));
var ItemContent = styled(Panel)(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  padding: ", " ", " ", " ", ";\n"], ["\n  padding: ", " ", " ", " ", ";\n"])), space(3), space(3), space(2), space(1));
var StyledButton = styled(Button)(templateObject_4 || (templateObject_4 = __makeTemplateObject(["\n  position: relative;\n"], ["\n  position: relative;\n"])));
var StyledAlert = styled(Alert)(templateObject_5 || (templateObject_5 = __makeTemplateObject(["\n  margin-bottom: ", ";\n"], ["\n  margin-bottom: ", ";\n"])), space(1));
var templateObject_1, templateObject_2, templateObject_3, templateObject_4, templateObject_5;
//# sourceMappingURL=index.jsx.map