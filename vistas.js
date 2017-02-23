//vistaEC, para obtener los tweets que sean solo de ecuador

function(doc) 
{
  if(doc.place.country_code=="EC")
    emit(doc.id, doc.created_at, doc.place.country_code, doc.text, doc.user.id, doc.user.friends_count);
}

//vista para sacar los datos mas importantes, que se querian pasar mediante mapeo al elasticsearch

function(doc) 
{
  if(doc.place.country_code=="EC")
    emit(doc.id, {"created_at":doc.created_at, "text":doc.text, "followers_count":doc.user.followers_count, "screen_name":doc.user.screen_name, "sentiment":doc.sentiment});
}