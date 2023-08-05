import { __read, __rest } from "tslib";
import { useState } from 'react';
import { t } from 'app/locale';
import Card from '../card';
import CardItem from '../cardItem';
import Form from './form';
function AppStoreCredentials(_a) {
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
      {data.issuer && <CardItem label={t('Issuer')} value={data.issuer}/>}
      {data.keyId && <CardItem label={t('Key Id')} value={data.keyId}/>}
      {((_b = data.app) === null || _b === void 0 ? void 0 : _b.name) && (<CardItem label={t('App Store Connect Application')} value={(_c = data.app) === null || _c === void 0 ? void 0 : _c.name}/>)}
    </Card>);
}
export default AppStoreCredentials;
//# sourceMappingURL=index.jsx.map