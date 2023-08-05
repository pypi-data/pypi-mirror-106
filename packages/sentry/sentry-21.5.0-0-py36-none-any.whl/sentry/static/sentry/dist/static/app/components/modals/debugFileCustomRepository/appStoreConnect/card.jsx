import { __makeTemplateObject } from "tslib";
import styled from '@emotion/styled';
import Button from 'app/components/button';
import { IconEdit, IconLock } from 'app/icons';
import { t } from 'app/locale';
import space from 'app/styles/space';
function Card(_a) {
    var children = _a.children, onEdit = _a.onEdit;
    return (<Wrapper>
      <IconWrapper>
        <IconLock size="lg"/>
      </IconWrapper>
      <Content>{children}</Content>
      <Action>
        <Button icon={<IconEdit />} label={t('Edit')} size="small" onClick={onEdit}/>
      </Action>
    </Wrapper>);
}
export default Card;
var Wrapper = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: grid;\n  grid-template-columns: max-content 1fr max-content;\n  grid-gap: ", ";\n"], ["\n  display: grid;\n  grid-template-columns: max-content 1fr max-content;\n  grid-gap: ", ";\n"])), space(1));
var Content = styled('div')(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: flex;\n  justify-content: center;\n  flex-direction: column;\n  font-size: ", ";\n"], ["\n  display: flex;\n  justify-content: center;\n  flex-direction: column;\n  font-size: ", ";\n"])), function (p) { return p.theme.fontSizeMedium; });
var IconWrapper = styled('div')(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  display: flex;\n  align-items: center;\n  padding: 0 ", ";\n"], ["\n  display: flex;\n  align-items: center;\n  padding: 0 ", ";\n"])), space(1.5));
var Action = styled('div')(templateObject_4 || (templateObject_4 = __makeTemplateObject(["\n  display: flex;\n  align-items: center;\n"], ["\n  display: flex;\n  align-items: center;\n"])));
var templateObject_1, templateObject_2, templateObject_3, templateObject_4;
//# sourceMappingURL=card.jsx.map