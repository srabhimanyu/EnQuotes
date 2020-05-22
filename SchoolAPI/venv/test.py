for s in rows:
        data= dict()
        for x in response_settings['SCHOOL_DATA']:
            if x == 'id' or x == 'city':
                data[x] = getattr(s,x)

            else:


