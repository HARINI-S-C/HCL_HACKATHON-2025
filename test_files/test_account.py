

#To test account creation

from app.schemas.account_schema import AccountResponse

# Simulate a SQLAlchemy ORM object
class AccountORM:
    def __init__(self, id, account_number, account_type, balance):
        self.id = id
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

# Create a fake account
fake_account = AccountORM(1, "SB1234567890", "savings", 1000)

# Convert ORM object to Pydantic schema
account_schema = AccountResponse.from_orm(fake_account)

print(account_schema)
print("✅ Works with Pydantic v2!")
