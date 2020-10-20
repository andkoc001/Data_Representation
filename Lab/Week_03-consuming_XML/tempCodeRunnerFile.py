        entryList = []

        # entryList.append(listing.find('TrainLatitude').string)

        for retrieveTag in retrieveTags:
            entryList.append(listing.find(retrieveTag).string)
            print(listing.find(retrieveTag).string)

            train_writer.writerow(entryList)

