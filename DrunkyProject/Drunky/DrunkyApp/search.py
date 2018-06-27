
def search_in_queryset(str, querySet):
    for set in querySet:
        if set.name.lower().find(str.lower()) == -1 and set.description.lower().find(str.lower()) == -1:
            querySet = querySet.exclude(name=set.name)
    return querySet