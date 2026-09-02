from django.shortcuts import render, get_object_or_404
from django.conf import settings
from google import genai

from files.models import Files


def file_summary(request, id):
    file_summary = None

    try:
        uploaded = Files.objects.get(id=id)

        if not uploaded.file:
            raise ValueError("No file is attached to this record.")

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        gemini_file = client.files.upload(
            file=uploaded.file.path
        )

        prompt = """
        Summarise the document.

        List all the important points clearly. Provide the summary as a html code.

        Keep the summary concise and easy to understand.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt, gemini_file]
        )

        file_summary = response.text

        file_summary = file_summary.replace("```html", "")
        file_summary = file_summary.replace("```", "")

    except Exception as e:
        file_summary = f"Error: {str(e)}"

    return render(request, "file_summary.html",{"summary": file_summary})