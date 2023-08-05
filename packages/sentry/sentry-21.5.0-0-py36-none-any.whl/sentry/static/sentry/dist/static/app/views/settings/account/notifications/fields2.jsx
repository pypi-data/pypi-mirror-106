import { t } from 'app/locale';
export var NOTIFICATION_SETTING_FIELDS = {
    alerts: {
        name: 'alerts',
        type: 'select',
        label: t('Issue Alert Notifications'),
        choices: [
            ['always', t('Always')],
            ['never', t('Never')],
        ],
    },
    deploy: {
        name: 'deploy',
        type: 'select',
        label: t('Deploy Notifications'),
        choices: [
            ['always', t('Always')],
            ['committed_only', t('Only Committed Issues')],
            ['never', t('Never')],
        ],
    },
    provider: {
        name: 'provider',
        type: 'select',
        label: t('Delivery Method'),
        choices: [
            ['email', t('Send to Email')],
            ['slack', t('Send to Slack')],
            ['email+slack', t('Send to Email and Slack')],
        ],
    },
    workflow: {
        name: 'workflow',
        type: 'select',
        label: t('Workflow Notifications'),
        choices: [
            ['always', t('Always')],
            ['subscribe_only', t('Only Subscribed Issues')],
            ['never', t('Never')],
        ],
    },
};
//# sourceMappingURL=fields2.jsx.map