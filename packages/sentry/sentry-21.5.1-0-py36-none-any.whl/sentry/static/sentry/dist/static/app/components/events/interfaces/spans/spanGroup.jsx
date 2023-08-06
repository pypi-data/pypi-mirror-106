import { __extends } from "tslib";
import { Component, Fragment } from 'react';
import { withScrollbarManager } from './scrollbarManager';
import SpanBar from './spanBar';
var SpanGroup = /** @class */ (function (_super) {
    __extends(SpanGroup, _super);
    function SpanGroup() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = {
            showSpanTree: true,
        };
        _this.toggleSpanTree = function () {
            _this.setState(function (state) { return ({
                showSpanTree: !state.showSpanTree,
            }); });
        };
        _this.renderSpanChildren = function () {
            if (!_this.state.showSpanTree) {
                return null;
            }
            return _this.props.renderedSpanChildren;
        };
        return _this;
    }
    SpanGroup.prototype.componentDidUpdate = function (_prevProps, prevState) {
        if (prevState.showSpanTree !== this.state.showSpanTree) {
            // Update horizontal scroll states after this subtree was either hidden or
            // revealed.
            this.props.updateScrollState();
        }
    };
    SpanGroup.prototype.render = function () {
        var _a = this.props, spanBarColour = _a.spanBarColour, spanBarHatch = _a.spanBarHatch, span = _a.span, numOfSpanChildren = _a.numOfSpanChildren, trace = _a.trace, isLast = _a.isLast, isRoot = _a.isRoot, continuingTreeDepths = _a.continuingTreeDepths, generateBounds = _a.generateBounds, treeDepth = _a.treeDepth, spanNumber = _a.spanNumber, isCurrentSpanFilteredOut = _a.isCurrentSpanFilteredOut, organization = _a.organization, event = _a.event;
        return (<Fragment>
        <SpanBar organization={organization} event={event} spanBarColour={spanBarColour} spanBarHatch={spanBarHatch} span={span} showSpanTree={this.state.showSpanTree} numOfSpanChildren={numOfSpanChildren} trace={trace} generateBounds={generateBounds} toggleSpanTree={this.toggleSpanTree} treeDepth={treeDepth} continuingTreeDepths={continuingTreeDepths} spanNumber={spanNumber} isLast={isLast} isRoot={isRoot} isCurrentSpanFilteredOut={isCurrentSpanFilteredOut}/>
        {this.renderSpanChildren()}
      </Fragment>);
    };
    return SpanGroup;
}(Component));
export default withScrollbarManager(SpanGroup);
//# sourceMappingURL=spanGroup.jsx.map