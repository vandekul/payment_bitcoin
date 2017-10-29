from openerp.addons.payment.models.payment_acquirer import ValidationError
from openerp.osv import osv
from openerp.tools.float_utils import float_compare
from openerp.osv import osv, fields
from openerp.tools.translate import _

import logging
import pprint

_logger = logging.getLogger(__name__)


class AcquirerBitcoin(osv.Model):
    _inherit = 'payment.acquirer'

    def _get_providers(self, cr, uid, context=None):
        providers = super(AcquirerBitcoin, self)._get_providers(cr, uid, context=context)
        providers.append(['bitcoin', 'Bitcoin'])
        return providers

    _columns = {
        'bitcoin_seed': fields.char(
        'Bitcoin Seed', groups='base.group_user',
        help='Bitcoin Seed is used to create ...'),
    }


    class TxPaypal(osv.Model):
        _inherit = 'payment.transaction'

        _columns = {
        'bitcoin_txn_type': fields.char('Transaction type'),
        }

