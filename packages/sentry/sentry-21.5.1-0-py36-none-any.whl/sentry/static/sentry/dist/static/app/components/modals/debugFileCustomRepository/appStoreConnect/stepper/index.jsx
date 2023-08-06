import { __read } from "tslib";
import { Fragment, useEffect, useRef, useState } from 'react';
import Step from './step';
function Stepper(_a) {
    var activeStep = _a.activeStep, steps = _a.steps, renderStepContent = _a.renderStepContent, renderStepActions = _a.renderStepActions;
    var _b = __read(useState([]), 2), stepHeights = _b[0], setStepHeights = _b[1];
    useEffect(function () {
        calcStepContentHeights();
    }, []);
    var wrapperRef = useRef(null);
    function calcStepContentHeights() {
        var stepperElement = wrapperRef.current;
        if (stepperElement) {
            var newStepHeights = steps.map(function (_step, index) { return stepperElement.children[index].offsetHeight; });
            setStepHeights(newStepHeights);
        }
    }
    return (<div ref={wrapperRef}>
      {steps.map(function (step, index) {
            var isActive = !stepHeights.length || activeStep === index;
            return (<Step key={step} label={step} activeStep={activeStep} isActive={isActive} height={!!stepHeights.length ? stepHeights[index] : undefined}>
            {isActive && (<Fragment>
                {renderStepContent(index)}
                {renderStepActions(index)}
              </Fragment>)}
          </Step>);
        })}
    </div>);
}
export default Stepper;
//# sourceMappingURL=index.jsx.map