async def on_page_context_created(page, context, metadata, **kwargs):
    token = metadata.get("token", "")
    await page.set_extra_http_headers({
        "X-Redmine-API-Key": "18a8a56d0ea5595d2aae1bd002ae8fef44259956"
    })
    return page
