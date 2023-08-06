import { __makeTemplateObject } from "tslib";
import styled from '@emotion/styled';
import { IconChevron } from 'app/icons';
import space from 'app/styles/space';
function Step(_a) {
    var children = _a.children, label = _a.label, activeStep = _a.activeStep, isActive = _a.isActive, height = _a.height;
    return (<Wrapper activeStep={activeStep} isActive={isActive} height={height}>
      <Connector>
        <IconChevron direction="right" size="sm" isCircled/>
      </Connector>
      <Content>
        {label}
        {children && <div>{children}</div>}
      </Content>
    </Wrapper>);
}
export default Step;
var Connector = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  padding: ", " ", " 0 ", ";\n"], ["\n  padding: ", " ", " 0 ", ";\n"])), space(0.5), space(1.5), space(1.5));
var getHeightStyle = function (isActive, height) {
    if (!height) {
        return '';
    }
    if (isActive) {
        return "\n      height: " + height + "px;\n    ";
    }
    return "\n    height: 26px;\n    :not(:last-child) {\n      height: 42px;\n    }\n  ";
};
var Wrapper = styled('div')(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: grid;\n  grid-template-columns: max-content 1fr;\n  position: relative;\n  color: ", ";\n\n  :not(:last-child) {\n    padding-bottom: ", ";\n    ", " {\n      :before {\n        content: ' ';\n        border-right: 1px ", " dashed;\n        position: absolute;\n        top: 28px;\n        left: ", ";\n        height: calc(100% - 28px);\n      }\n    }\n\n    :nth-child(-n + ", ") {\n      ", " {\n        :before {\n          border-color: ", ";\n        }\n      }\n    }\n  }\n\n  :nth-child(-n + ", ") {\n    color: ", ";\n  }\n\n  transition: height 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;\n  ", "\n"], ["\n  display: grid;\n  grid-template-columns: max-content 1fr;\n  position: relative;\n  color: ", ";\n\n  :not(:last-child) {\n    padding-bottom: ", ";\n    ", " {\n      :before {\n        content: ' ';\n        border-right: 1px ", " dashed;\n        position: absolute;\n        top: 28px;\n        left: ", ";\n        height: calc(100% - 28px);\n      }\n    }\n\n    :nth-child(-n + ", ") {\n      ", " {\n        :before {\n          border-color: ", ";\n        }\n      }\n    }\n  }\n\n  :nth-child(-n + ", ") {\n    color: ", ";\n  }\n\n  transition: height 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;\n  ", "\n"])), function (p) { return p.theme.gray200; }, space(2), Connector, function (p) { return p.theme.gray300; }, space(3), function (p) { return p.activeStep + 1; }, Connector, function (p) { return p.theme.gray500; }, function (p) { return p.activeStep + 1; }, function (p) { return p.theme.gray500; }, function (p) { return getHeightStyle(p.isActive, p.height); });
var Content = styled('div')(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  display: grid;\n  grid-gap: ", ";\n"], ["\n  display: grid;\n  grid-gap: ", ";\n"])), space(1.5));
var templateObject_1, templateObject_2, templateObject_3;
//# sourceMappingURL=step.jsx.map