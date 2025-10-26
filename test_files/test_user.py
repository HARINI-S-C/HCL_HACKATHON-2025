from app.schemas.users_schemas import UserCreate, UserResponse

# Simulate a SQLAlchemy ORM object
class UserORM:
    def __init__(self, id, full_name, email, role, kyc_status):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.role = role
        self.kyc_status = kyc_status

# Create a fake user
fake_user = UserORM(
    id=1,
    full_name="John Doe",
    email="john.doe@example.com",
    role="user",
    kyc_status="verified"
)

# Convert ORM object to Pydantic model
user_response = UserResponse.from_orm(fake_user)

# Print results
print(user_response)
print("✅ UserResponse schema works correctly with ORM")
