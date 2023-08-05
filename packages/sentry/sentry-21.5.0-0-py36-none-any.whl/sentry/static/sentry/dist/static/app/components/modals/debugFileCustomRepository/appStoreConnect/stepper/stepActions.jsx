import { __makeTemplateObject } from "tslib";
import styled from '@emotion/styled';
import Button from 'app/components/button';
import ButtonBar from 'app/components/buttonBar';
import LoadingIndicator from 'app/components/loadingIndicator';
import { t } from 'app/locale';
function StepActions(_a) {
    var primaryButtonDisabled = _a.primaryButtonDisabled, isLoading = _a.isLoading, onFinish = _a.onFinish, onCancel = _a.onCancel, onGoBack = _a.onGoBack, onGoNext = _a.onGoNext;
    return (<Wrapper>
      <ButtonBar gap={1}>
        {onCancel && (<Button size="small" onClick={onCancel}>
            {t('Cancel')}
          </Button>)}
        {onGoBack && (<Button size="small" onClick={onGoBack}>
            {t('Back')}
          </Button>)}
        {onGoNext ? (<StyledButton size="small" priority="primary" onClick={onGoNext} disabled={primaryButtonDisabled}>
            {isLoading && (<LoadingIndicatorWrapper>
                <LoadingIndicator mini/>
              </LoadingIndicatorWrapper>)}
            {t('Next')}
          </StyledButton>) : (<StyledButton size="small" priority="primary" onClick={onFinish} disabled={primaryButtonDisabled}>
            {isLoading && (<LoadingIndicatorWrapper>
                <LoadingIndicator mini/>
              </LoadingIndicatorWrapper>)}
            {t('Finish')}
          </StyledButton>)}
      </ButtonBar>
    </Wrapper>);
}
export default StepActions;
var Wrapper = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: flex;\n"], ["\n  display: flex;\n"])));
var StyledButton = styled(Button)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  position: relative;\n"], ["\n  position: relative;\n"])));
var LoadingIndicatorWrapper = styled('div')(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  height: 100%;\n  position: absolute;\n  width: 100%;\n  top: 0;\n  left: 0;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n"], ["\n  height: 100%;\n  position: absolute;\n  width: 100%;\n  top: 0;\n  left: 0;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n"])));
var templateObject_1, templateObject_2, templateObject_3;
//# sourceMappingURL=stepActions.jsx.map