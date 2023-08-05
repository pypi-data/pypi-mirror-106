# IMPORT ORDER MATTERS!

# constants used by MetaCI
FAILED_TO_CREATE_SCRATCH_ORG = "Failed to create scratch org"

from cumulusci.core.config.BaseConfig import BaseConfig

# inherit from BaseConfig


class ConnectedAppOAuthConfig(BaseConfig):
    """Salesforce Connected App OAuth configuration"""

    pass


class FlowConfig(BaseConfig):
    """A flow with its configuration merged"""

    pass


from cumulusci.core.config.OrgConfig import OrgConfig


class ServiceConfig(BaseConfig):
    def __init__(self, config, name=None, keychain=None):
        """Services may need access to a keychain and the alias of their service."""
        super().__init__(config, keychain)


class TaskConfig(BaseConfig):
    """A task with its configuration merged"""

    pass


from cumulusci.core.config.BaseTaskFlowConfig import BaseTaskFlowConfig


# inherit from BaseTaskFlowConfig
from cumulusci.core.config.project_config import BaseProjectConfig

# inherit from OrgConfig
from cumulusci.core.config.sfdx_org_config import SfdxOrgConfig

# inherit from SfdxOrgConfig
from cumulusci.core.config.ScratchOrgConfig import ScratchOrgConfig

# inherit from BaseProjectConfig
from cumulusci.core.config.universal_config import UniversalConfig


__all__ = (
    "FAILED_TO_CREATE_SCRATCH_ORG",
    "BaseConfig",
    "ConnectedAppOAuthConfig",
    "FlowConfig",
    "OrgConfig",
    "ServiceConfig",
    "TaskConfig",
    "BaseTaskFlowConfig",
    "BaseProjectConfig",
    "SfdxOrgConfig",
    "ScratchOrgConfig",
    "UniversalConfig",
)
