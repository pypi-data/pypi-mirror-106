import { __extends, __makeTemplateObject, __read } from "tslib";
import * as React from 'react';
import styled from '@emotion/styled';
import pick from 'lodash/pick';
import { openDiffModal } from 'app/actionCreators/modal';
import Button from 'app/components/button';
import Confirm from 'app/components/confirm';
import { PanelHeader } from 'app/components/panels';
import { t, tct } from 'app/locale';
import GroupingStore from 'app/stores/groupingStore';
import space from 'app/styles/space';
import withOrganization from 'app/utils/withOrganization';
var MergedToolbar = /** @class */ (function (_super) {
    __extends(MergedToolbar, _super);
    function MergedToolbar() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = _this.getInitialState();
        _this.listener = GroupingStore.listen(function (data) { return _this.onGroupChange(data); }, undefined);
        _this.onGroupChange = function (updateObj) {
            var allowedKeys = [
                'unmergeLastCollapsed',
                'unmergeDisabled',
                'unmergeList',
                'enableFingerprintCompare',
            ];
            _this.setState(pick(updateObj, allowedKeys));
        };
        _this.handleShowDiff = function (event) {
            var _a = _this.props, groupId = _a.groupId, project = _a.project, orgId = _a.orgId;
            var unmergeList = _this.state.unmergeList;
            var entries = unmergeList.entries();
            // `unmergeList` should only have 2 items in map
            if (unmergeList.size !== 2) {
                return;
            }
            // only need eventId, not fingerprint
            var _b = __read(Array.from(entries).map(function (_a) {
                var _b = __read(_a, 2), eventId = _b[1];
                return eventId;
            }), 2), baseEventId = _b[0], targetEventId = _b[1];
            openDiffModal({
                targetIssueId: groupId,
                project: project,
                baseIssueId: groupId,
                orgId: orgId,
                baseEventId: baseEventId,
                targetEventId: targetEventId,
            });
            event.stopPropagation();
        };
        return _this;
    }
    MergedToolbar.prototype.getInitialState = function () {
        var unmergeList = GroupingStore.unmergeList, unmergeLastCollapsed = GroupingStore.unmergeLastCollapsed, unmergeDisabled = GroupingStore.unmergeDisabled, enableFingerprintCompare = GroupingStore.enableFingerprintCompare;
        return {
            enableFingerprintCompare: enableFingerprintCompare,
            unmergeList: unmergeList,
            unmergeLastCollapsed: unmergeLastCollapsed,
            unmergeDisabled: unmergeDisabled,
        };
    };
    MergedToolbar.prototype.componentWillUnmount = function () {
        var _a;
        (_a = this.listener) === null || _a === void 0 ? void 0 : _a.call(this);
    };
    MergedToolbar.prototype.render = function () {
        var _a;
        var _b = this.props, onUnmerge = _b.onUnmerge, onSplit = _b.onSplit, onToggleCollapse = _b.onToggleCollapse, organization = _b.organization;
        var hasGroupingTreeFeature = (_a = organization === null || organization === void 0 ? void 0 : organization.features) === null || _a === void 0 ? void 0 : _a.includes('grouping-tree-ui');
        var _c = this.state, unmergeList = _c.unmergeList, unmergeLastCollapsed = _c.unmergeLastCollapsed, unmergeDisabled = _c.unmergeDisabled, enableFingerprintCompare = _c.enableFingerprintCompare;
        var unmergeCount = (unmergeList && unmergeList.size) || 0;
        return (<PanelHeader hasButtons>
        <div>
          <Confirm disabled={unmergeDisabled} onConfirm={onUnmerge} message={t('These events will be unmerged and grouped into a new issue. Are you sure you want to unmerge these events?')}>
            <Button size="small" title={tct('Unmerging [unmergeCount] events', { unmergeCount: unmergeCount })}>
              {t('Unmerge')} ({unmergeCount || 0})
            </Button>
          </Confirm>

          {hasGroupingTreeFeature && (<Confirm onConfirm={onSplit} message={t('These events will be grouped into a new issue by more specific criteria (for instance more frames). Are you sure you want to split them out of the existing issue?')}>
              <Button size="small" title={tct('Splitting out [unmergeCount] events', { unmergeCount: unmergeCount })}>
                {t('Split')} ({unmergeCount || 0})
              </Button>
            </Confirm>)}

          <CompareButton size="small" disabled={!enableFingerprintCompare} onClick={this.handleShowDiff}>
            {t('Compare')}
          </CompareButton>
        </div>
        <Button size="small" onClick={onToggleCollapse}>
          {unmergeLastCollapsed ? t('Expand All') : t('Collapse All')}
        </Button>
      </PanelHeader>);
    };
    return MergedToolbar;
}(React.Component));
export default withOrganization(MergedToolbar);
var CompareButton = styled(Button)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  margin-left: ", ";\n"], ["\n  margin-left: ", ";\n"])), space(1));
var templateObject_1;
//# sourceMappingURL=mergedToolbar.jsx.map