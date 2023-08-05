import { __assign, __makeTemplateObject } from "tslib";
import React from 'react';
import { withRouter } from 'react-router';
import { css } from '@emotion/react';
import { getDebugSourceName } from 'app/data/debugFileSources';
import { tct } from 'app/locale';
import FieldFromConfig from 'app/views/settings/components/forms/fieldFromConfig';
import Form from 'app/views/settings/components/forms/form';
import AppStoreConnect from './appStoreConnect';
import { getFormFields } from './utils';
function DebugFileCustomRepository(_a) {
    var closeModal = _a.closeModal, Header = _a.Header, Body = _a.Body, Footer = _a.Footer, onSave = _a.onSave, sourceConfig = _a.sourceConfig, sourceType = _a.sourceType, _b = _a.params, orgId = _b.orgId, projectId = _b.projectId;
    function handleSave(data) {
        onSave(__assign(__assign({}, data), { type: sourceType }));
        closeModal();
    }
    function renderForm() {
        if (sourceType === 'appStoreConnect') {
            return (<AppStoreConnect Body={Body} Footer={Footer} closeModal={closeModal} orgSlug={orgId} projectSlug={projectId} onSubmit={handleSave} initialData={sourceConfig}/>);
        }
        var fields = getFormFields(sourceType);
        if (!fields) {
            return null;
        }
        return (<Form allowUndo requireChanges initialData={sourceConfig} onSubmit={handleSave} footerClass="modal-footer">
        {fields.map(function (field, i) { return (<FieldFromConfig key={field.name || i} field={field} inline={false} stacked/>); })}
      </Form>);
    }
    var headerText = sourceConfig ? 'Update [name] Repository' : 'Add [name] Repository';
    return (<React.Fragment>
      <Header closeButton>
        {tct(headerText, { name: getDebugSourceName(sourceType) })}
      </Header>
      {renderForm()}
    </React.Fragment>);
}
export default withRouter(DebugFileCustomRepository);
export var modalCss = css(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  width: 100%;\n  max-width: 680px;\n"], ["\n  width: 100%;\n  max-width: 680px;\n"])));
var templateObject_1;
//# sourceMappingURL=index.jsx.map