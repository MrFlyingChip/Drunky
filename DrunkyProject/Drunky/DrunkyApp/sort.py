
def sort_query_set(sortType, querySet):
    if sortType == 'By favourites (ascending)':
        return querySet.order_by('favourites')
    elif sortType == 'By favourites (descending)':
        return querySet.order_by('-favourites')
    elif sortType == 'By popularity (descending)':
        return querySet.order_by('-likes')
    elif sortType == 'By popularity (ascending)':
        return querySet.order_by('likes')
    else:
        return querySet
