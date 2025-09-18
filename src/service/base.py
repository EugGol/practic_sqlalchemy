from src.domain.protocols import UnitOfWork


class BaseService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
