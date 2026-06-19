export async function onRequest(context) {
  const url = new URL(context.request.url);

  if (url.hostname === 'kalindimarketing.com') {
    url.protocol = 'https:';
    url.hostname = 'www.kalindimarketing.com';
    return Response.redirect(url.toString(), 301);
  }

  return context.next();
}
