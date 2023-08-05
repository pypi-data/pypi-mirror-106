import { __read, __rest } from "tslib";
import { useState } from 'react';
import { t } from 'app/locale';
import Card from '../card';
import CardItem from '../cardItem';
import Form from './form';
function ItunesCredentials(_a) {
    var _b, _c;
    var data = _a.data, isUpdating = _a.isUpdating, onReset = _a.onReset, props = __rest(_a, ["data", "isUpdating", "onReset"]);
    var _d = __read(useState(!isUpdating), 2), isEditing = _d[0], setIsEditing = _d[1];
    function handleSwitchToReadMode() {
        setIsEditing(false);
    }
    function handleCancel() {
        setIsEditing(false);
        onReset();
    }
    if (isEditing) {
        return (<Form {...props} data={data} onSwitchToReadMode={handleSwitchToReadMode} onCancel={isUpdating ? handleCancel : undefined}/>);
    }
    return (<Card onEdit={function () { return setIsEditing(true); }}>
      {data.username && <CardItem label={t('User')} value={data.username}/>}
      {((_b = data.org) === null || _b === void 0 ? void 0 : _b.name) && (<CardItem label={t('iTunes Organization')} value={(_c = data.org) === null || _c === void 0 ? void 0 : _c.name}/>)}
    </Card>);
}
export default ItunesCredentials;
//# sourceMappingURL=index.jsx.map