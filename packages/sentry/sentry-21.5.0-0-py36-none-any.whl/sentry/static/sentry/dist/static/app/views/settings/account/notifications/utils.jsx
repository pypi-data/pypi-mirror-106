import { __read, __values } from "tslib";
// Which fine tuning parts are grouped by project
export var isGroupedByProject = function (type) {
    return ['alerts', 'email', 'workflow'].includes(type);
};
export var groupByOrganization = function (projects) {
    return projects.reduce(function (acc, project) {
        var orgSlug = project.organization.slug;
        if (acc.hasOwnProperty(orgSlug)) {
            acc[orgSlug].projects.push(project);
        }
        else {
            acc[orgSlug] = {
                organization: project.organization,
                projects: [project],
            };
        }
        return acc;
    }, {});
};
export var getFallBackValue = function (notificationType) {
    switch (notificationType) {
        case 'alerts':
            return 'always';
        case 'deploy':
            return 'committed_only';
        case 'workflow':
            return 'subscribe_only';
        default:
            return '';
    }
};
export var providerListToString = function (providers) {
    return providers.sort().join('+');
};
export var getChoiceString = function (choices, key) {
    if (!choices) {
        return 'default';
    }
    var found = choices.find(function (row) { return row[0] === key; });
    if (!found) {
        throw new Error("Could not find " + key);
    }
    return found[1];
};
export var backfillMissingProvidersWithFallback = function (data, providerList, fallbackValue) {
    var e_1, _a, e_2, _b;
    /**
     * Transform `data` to include only providers expected in `providerList`.
     * Everything not in that list is set to "never". Missing values will be
     * backfilled either with a current value from `data` or `fallbackValue` if
     * none are present.
     *
     * For example:
     * f({}, ["email"], "sometimes") = {"email": "sometimes"}
     *
     * f({"email": "always", pagerduty: "always"}, ["email", "slack"], "sometimes") =
     * {"email": "always", "slack": "always", "pagerduty": "never"}
     */
    var entries = [];
    var fallback = fallbackValue;
    try {
        for (var _c = __values(Object.entries(data)), _d = _c.next(); !_d.done; _d = _c.next()) {
            var _e = __read(_d.value, 2), provider = _e[0], previousValue = _e[1];
            fallback = previousValue;
            entries.push([provider, providerList.includes(provider) ? previousValue : 'never']);
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
        }
        finally { if (e_1) throw e_1.error; }
    }
    try {
        for (var providerList_1 = __values(providerList), providerList_1_1 = providerList_1.next(); !providerList_1_1.done; providerList_1_1 = providerList_1.next()) {
            var provider = providerList_1_1.value;
            entries.push([provider, fallback]);
        }
    }
    catch (e_2_1) { e_2 = { error: e_2_1 }; }
    finally {
        try {
            if (providerList_1_1 && !providerList_1_1.done && (_b = providerList_1.return)) _b.call(providerList_1);
        }
        finally { if (e_2) throw e_2.error; }
    }
    return Object.fromEntries(entries);
};
//# sourceMappingURL=utils.jsx.map