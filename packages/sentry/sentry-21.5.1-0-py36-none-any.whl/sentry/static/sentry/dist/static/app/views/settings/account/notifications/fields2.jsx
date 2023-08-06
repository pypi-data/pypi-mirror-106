import { t } from 'app/locale';
export var NOTIFICATION_SETTING_FIELDS = {
    alerts: {
        name: 'alerts',
        type: 'select',
        label: t('Issue Alert Notifications'),
        choices: [
            ['always', t('On')],
            ['never', t('Off')],
        ],
    },
    deploy: {
        name: 'deploy',
        type: 'select',
        label: t('Deploy Notifications'),
        choices: [
            ['always', t('On')],
            ['committed_only', t('Only Committed Issues')],
            ['never', t('Off')],
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
            ['always', t('On')],
            ['subscribe_only', t('Only Subscribed Issues')],
            ['never', t('Off')],
        ],
    },
};
//# sourceMappingURL=fields2.jsx.map