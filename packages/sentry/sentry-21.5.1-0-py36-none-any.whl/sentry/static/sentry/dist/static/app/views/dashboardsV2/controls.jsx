import { __assign, __extends, __makeTemplateObject } from "tslib";
import * as React from 'react';
import { browserHistory } from 'react-router';
import styled from '@emotion/styled';
import Feature from 'app/components/acl/feature';
import FeatureDisabled from 'app/components/acl/featureDisabled';
import Button from 'app/components/button';
import ButtonBar from 'app/components/buttonBar';
import Confirm from 'app/components/confirm';
import SelectControl from 'app/components/forms/selectControl';
import Hovercard from 'app/components/hovercard';
import { IconAdd, IconEdit } from 'app/icons';
import { t } from 'app/locale';
import space from 'app/styles/space';
import { DashboardState } from './types';
var Controls = /** @class */ (function (_super) {
    __extends(Controls, _super);
    function Controls() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Controls.prototype.render = function () {
        var _a = this.props, dashboardState = _a.dashboardState, dashboards = _a.dashboards, dashboard = _a.dashboard, organization = _a.organization, onEdit = _a.onEdit, onCreate = _a.onCreate, onCancel = _a.onCancel, onCommit = _a.onCommit, onDelete = _a.onDelete;
        var cancelButton = (<Button data-test-id="dashboard-cancel" onClick={function (e) {
                e.preventDefault();
                onCancel();
            }}>
        {t('Cancel')}
      </Button>);
        if ([DashboardState.EDIT, DashboardState.PENDING_DELETE].includes(dashboardState)) {
            return (<StyledButtonBar gap={1} key="edit-controls">
          {cancelButton}
          <Confirm priority="danger" message={t('Are you sure you want to delete this dashboard?')} onConfirm={onDelete} disabled={dashboards.length <= 1}>
            <Button data-test-id="dashboard-delete" priority="danger">
              {t('Delete')}
            </Button>
          </Confirm>
          <Button data-test-id="dashboard-commit" onClick={function (e) {
                    e.preventDefault();
                    onCommit();
                }} priority="primary">
            {t('Save and Finish')}
          </Button>
        </StyledButtonBar>);
        }
        if (dashboardState === 'create') {
            return (<StyledButtonBar gap={1} key="create-controls">
          {cancelButton}
          <Button data-test-id="dashboard-commit" onClick={function (e) {
                    e.preventDefault();
                    onCommit();
                }} priority="primary">
            {t('Save and Finish')}
          </Button>
        </StyledButtonBar>);
        }
        var dropdownOptions = dashboards.map(function (item) {
            return {
                label: item.title,
                value: item,
            };
        });
        var currentOption = undefined;
        if (dashboard) {
            currentOption = {
                label: dashboard.title,
                value: __assign(__assign({}, dashboard), { widgetDisplay: dashboard.widgets.map(function (w) { return w.displayType; }) }),
            };
        }
        else if (dropdownOptions.length) {
            currentOption = dropdownOptions[0];
        }
        var dashboardSelect = organization.features.includes('dashboards-edit') &&
            !organization.features.includes('dashboards-manage') ? (<DashboardSelect>
          <SelectControl key="select" name="parameter" placeholder={t('Select Dashboard')} options={dropdownOptions} value={currentOption} onChange={function (_a) {
                var value = _a.value;
                browserHistory.push({
                    pathname: "/organizations/" + organization.slug + "/dashboard/" + value.id + "/",
                    // TODO(mark) should this retain global selection?
                    query: {},
                });
            }}/>
        </DashboardSelect>) : null;
        var createButton = organization.features.includes('dashboards-edit') &&
            !organization.features.includes('dashboards-manage') ? (<Button data-test-id="dashboard-create" onClick={function (e) {
                e.preventDefault();
                onCreate();
            }} icon={<IconAdd size="xs" isCircled/>}>
          {t('Create Dashboard')}
        </Button>) : null;
        return (<StyledButtonBar gap={1} key="controls">
        {dashboardSelect}
        {createButton}
        <DashboardEditFeature>
          {function (hasFeature) { return (<Button data-test-id="dashboard-edit" onClick={function (e) {
                    e.preventDefault();
                    onEdit();
                }} priority="primary" icon={<IconEdit size="xs"/>} disabled={!hasFeature}>
              {t('Edit Dashboard')}
            </Button>); }}
        </DashboardEditFeature>
      </StyledButtonBar>);
    };
    return Controls;
}(React.Component));
var DashboardEditFeature = function (_a) {
    var children = _a.children;
    var noFeatureMessage = t('Requires dashboard editing.');
    var renderDisabled = function (p) { return (<Hovercard body={<FeatureDisabled features={p.features} hideHelpToggle message={noFeatureMessage} featureName={noFeatureMessage}/>}>
      {p.children(p)}
    </Hovercard>); };
    return (<Feature hookName="feature-disabled:dashboards-edit" features={['organizations:dashboards-edit']} renderDisabled={renderDisabled}>
      {function (_a) {
        var hasFeature = _a.hasFeature;
        return children(hasFeature);
    }}
    </Feature>);
};
var DashboardSelect = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  min-width: 200px;\n  font-size: ", ";\n"], ["\n  min-width: 200px;\n  font-size: ", ";\n"])), function (p) { return p.theme.fontSizeMedium; });
var StyledButtonBar = styled(ButtonBar)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  @media (max-width: ", ") {\n    grid-auto-flow: row;\n    grid-row-gap: ", ";\n    width: 100%;\n  }\n"], ["\n  @media (max-width: ", ") {\n    grid-auto-flow: row;\n    grid-row-gap: ", ";\n    width: 100%;\n  }\n"])), function (p) { return p.theme.breakpoints[0]; }, space(1));
export default Controls;
var templateObject_1, templateObject_2;
//# sourceMappingURL=controls.jsx.map