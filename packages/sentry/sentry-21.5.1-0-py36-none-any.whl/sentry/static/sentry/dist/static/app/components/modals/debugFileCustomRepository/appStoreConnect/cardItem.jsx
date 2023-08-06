import { __makeTemplateObject } from "tslib";
import styled from '@emotion/styled';
import space from 'app/styles/space';
function CardItem(_a) {
    var label = _a.label, value = _a.value;
    return (<Wrapper>
      <strong>{label + ":"}</strong>
      {value}
    </Wrapper>);
}
export default CardItem;
var Wrapper = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: grid;\n  grid-template-columns: max-content 1fr;\n  grid-gap: ", ";\n"], ["\n  display: grid;\n  grid-template-columns: max-content 1fr;\n  grid-gap: ", ";\n"])), space(1));
var templateObject_1;
//# sourceMappingURL=cardItem.jsx.map