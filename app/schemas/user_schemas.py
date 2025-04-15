from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid
import re
from app.utils.nickname_gen import generate_nickname

class UserRole(str, Enum):
    ANONYMOUS = "ANONYMOUS"
    AUTHENTICATED = "AUTHENTICATED"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"

def validate_url(url: Optional[str]) -> Optional[str]:
    if url is None:
        return url
    url_pattern = r'^https?:\/\/[^\s/$.?#].[^\s]*$'
    if not re.match(url_pattern, url):
        raise ValueError('Invalid URL format')
    return url

# Validating username to meet certain rules
def validate_nickname(nickname: str) -> str:
    if len(nickname) < 3 or len(nickname) > 20:
        raise ValueError("Nickname must be between 3 and 20 characters.")
    if not re.match(r'^[\w-]+$', nickname):
        raise ValueError("Nickname can only contain letters, numbers, underscores, and hyphens.")
    return nickname

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    nickname: str = Field(default_factory=generate_nickname, min_length=3, max_length=20, example="john_doe")
    first_name: str = Field(default="First", example="John")
    last_name: str = Field(default="Last", example="Doe")
    bio: Optional[str] = Field(None, example="Experienced software developer.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profile.jpg")
    linkedin_profile_url: Optional[str] = Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")

    # Apply URL validation
    _validate_urls = validator('profile_picture_url', 'linkedin_profile_url', 'github_profile_url', pre=True, allow_reuse=True)(validate_url)
    
    # Apply Nickname validation
    _validate_nickname = validator('nickname', pre=True, allow_reuse=True)(validate_nickname)

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str = Field(..., example="Secure*1234")

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(None, example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, max_length=20, pattern=r'^[\w-]+$', example="john_doe")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Updated bio")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profile.jpg")
    linkedin_profile_url: Optional[str] = Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")

    @root_validator(pre=True)
    def check_at_least_one_value(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field must be provided for the update")
        return values

class UserResponse(UserBase):
    id: uuid.UUID = Field(..., example=str(uuid.uuid4()))
    role: UserRole = Field(default=UserRole.AUTHENTICATED, example="AUTHENTICATED")
    is_professional: Optional[bool] = Field(default=False, example=True)

    class Config:
        json_encoders = {
            uuid.UUID: lambda v: str(v)  # Ensures UUID is serialized as a string
        }

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")

class ErrorResponse(BaseModel):
    error: str = Field(..., example="Not Found")
    details: Optional[str] = Field(None, example="Resource not found.")

class UserListResponse(BaseModel):
    items: List[UserResponse] = Field(..., example=[])
    total: int = Field(..., example=100)
    page: int = Field(..., example=1)
    size: int = Field(..., example=10)