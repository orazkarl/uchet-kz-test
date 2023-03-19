import os
from datetime import datetime

from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette import status

from app.core.config import settings
from app.services.s3_bucket import S3Service

router = APIRouter()


@router.post("/upload", status_code=200)
async def upload(
        fileobject: UploadFile = File(...)
):
    filename = fileobject.filename
    current_time = datetime.now()
    split_file_name = os.path.splitext(filename)
    file_name_unique = str(current_time.timestamp()).replace('.','')
    file_extension = split_file_name[1]
    data = fileobject.file._file
    s3_client = S3Service(
        settings.AWS_ACCESS_KEY_ID,
        settings.AWS_SECRET_ACCESS_KEY,
        settings.AWS_REGION
    )
    result = await s3_client.upload_file(
        bucket=settings.S3_BUCKET,
        key=settings.S3_KEY + file_name_unique + file_extension,
        fileobject=data
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to upload in S3"
        )
    image_url = f"https://{settings.S3_BUCKET}.s3.{settings.AWS_REGION}.amazonaws.com/{settings.S3_KEY}{file_name_unique + file_extension}"
    return {"image_url": image_url}

