import { __extends, __makeTemplateObject } from "tslib";
import * as React from 'react';
import { withRouter } from 'react-router';
import styled from '@emotion/styled';
import moment from 'moment';
import AreaChart from 'app/components/charts/areaChart';
import ChartZoom from 'app/components/charts/chartZoom';
import { truncationFormatter } from 'app/components/charts/utils';
import Count from 'app/components/count';
import { Panel, PanelBody, PanelFooter } from 'app/components/panels';
import Placeholder from 'app/components/placeholder';
import { t, tct } from 'app/locale';
import space from 'app/styles/space';
import withApi from 'app/utils/withApi';
import { DisplayOption } from 'app/views/releases/list/utils';
var ReleaseAdoptionChart = /** @class */ (function (_super) {
    __extends(ReleaseAdoptionChart, _super);
    function ReleaseAdoptionChart() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = {
            width: -1,
            height: -1,
        };
        _this.ref = null;
        /**
         * Syncs component state with the chart's width/heights
         */
        _this.updateDimensions = function () {
            var _a, _b;
            var chartRef = (_b = (_a = _this.ref) === null || _a === void 0 ? void 0 : _a.getEchartsInstance) === null || _b === void 0 ? void 0 : _b.call(_a);
            if (!chartRef) {
                return;
            }
            var width = chartRef.getWidth();
            var height = chartRef.getHeight();
            if (width !== _this.state.width || height !== _this.state.height) {
                _this.setState({
                    width: width,
                    height: height,
                });
            }
        };
        _this.handleRef = function (ref) {
            if (ref && !_this.ref) {
                _this.ref = ref;
                _this.updateDimensions();
            }
            if (!ref) {
                _this.ref = null;
            }
        };
        return _this;
    }
    ReleaseAdoptionChart.prototype.renderEmpty = function () {
        return (<Panel>
        <ChartBody withPadding>
          <ChartHeader>
            <Placeholder height="24px"/>
          </ChartHeader>
          <Placeholder height="200px"/>
        </ChartBody>
        <ChartFooter>
          <Placeholder height="24px"/>
        </ChartFooter>
      </Panel>);
    };
    ReleaseAdoptionChart.prototype.render = function () {
        var _a = this.props, showPlaceholders = _a.showPlaceholders, releases = _a.releases, project = _a.project, activeDisplay = _a.activeDisplay, router = _a.router, selection = _a.selection, getHealthData = _a.getHealthData;
        var _b = selection.datetime, start = _b.start, end = _b.end, period = _b.period, utc = _b.utc;
        if (showPlaceholders) {
            return this.renderEmpty();
        }
        var get24hCountByProject = getHealthData.get24hCountByProject(Number(project.id), activeDisplay);
        var releasesSeries = releases.map(function (release) {
            var releaseVersion = release.version;
            var timeSeries = getHealthData.getTimeSeries(releaseVersion, Number(project.id), activeDisplay);
            var releaseData = timeSeries[0].data;
            var totalData = timeSeries[1].data;
            return {
                data: releaseData.map(function (d, i) { return ({
                    name: d.name,
                    value: d.value > 0 && totalData[i].value > 0
                        ? (100 * d.value) / totalData[i].value
                        : 0,
                }); }),
                seriesName: releaseVersion,
            };
        });
        return (<Panel>
        <ChartBody withPadding>
          <ChartHeader>
            <ChartTitle>
              {activeDisplay === DisplayOption.USERS
                ? t('Releases Adopted by Users')
                : t('Releases Adopted by Sessions')}
            </ChartTitle>
          </ChartHeader>
          <ChartZoom router={router} period={period} utc={utc} start={start} end={end}>
            {function (zoomRenderProps) { return (<AreaChart {...zoomRenderProps} series={releasesSeries} yAxis={{
                    min: 0,
                    max: 100,
                    type: 'value',
                    interval: 10,
                    splitNumber: 10,
                    data: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                    axisLabel: {
                        formatter: '{value}%',
                    },
                }} tooltip={{
                    formatter: function (seriesParams) {
                        var series = Array.isArray(seriesParams)
                            ? seriesParams
                            : [seriesParams];
                        var timestamp = series[0].data[0];
                        var topSeries = series
                            .sort(function (a, b) { return b.data[1] - a.data[1]; })
                            .slice(0, 3);
                        var topSum = topSeries.reduce(function (acc, s) { return acc + s.data[1]; }, 0);
                        if (series.length - topSeries.length > 0) {
                            topSeries.push({
                                seriesName: t('%s Others', series.length - topSeries.length),
                                data: [timestamp, 100 - topSum],
                                marker: '<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;"></span>',
                            });
                        }
                        return [
                            '<div class="tooltip-series">',
                            topSeries
                                .map(function (s) {
                                return "<div><span class=\"tooltip-label\">" + s.marker + "<strong>" + (s.seriesName && truncationFormatter(s.seriesName, 12)) + "</strong></span>" + s.data[1].toFixed(2) + "%</div>";
                            })
                                .join(''),
                            '</div>',
                            "<div class=\"tooltip-date\">" + moment(timestamp).format('MMM D, YYYY LT') + "</div>",
                            "<div class=\"tooltip-arrow\"></div>",
                        ].join('');
                    },
                }}/>); }}
          </ChartZoom>
        </ChartBody>
        {<ChartFooter>
            {tct('Total [display] [count]', {
                    display: activeDisplay === DisplayOption.USERS ? 'Users' : 'Sessions',
                    count: <Count value={get24hCountByProject !== null && get24hCountByProject !== void 0 ? get24hCountByProject : 0}/>,
                })}
          </ChartFooter>}
      </Panel>);
    };
    return ReleaseAdoptionChart;
}(React.PureComponent));
export default withApi(withRouter(ReleaseAdoptionChart));
var ChartHeader = styled('div')(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  margin-bottom: ", ";\n"], ["\n  margin-bottom: ", ";\n"])), space(1));
var ChartTitle = styled('header')(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: flex;\n  flex-direction: row;\n"], ["\n  display: flex;\n  flex-direction: row;\n"])));
var ChartBody = styled(PanelBody)(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  padding-bottom: 0;\n"], ["\n  padding-bottom: 0;\n"])));
var ChartFooter = styled(PanelFooter)(templateObject_4 || (templateObject_4 = __makeTemplateObject(["\n  display: flex;\n  align-items: center;\n  padding: ", " 20px;\n"], ["\n  display: flex;\n  align-items: center;\n  padding: ", " 20px;\n"])), space(1));
var templateObject_1, templateObject_2, templateObject_3, templateObject_4;
//# sourceMappingURL=releaseAdoptionChart.jsx.map