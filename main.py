from difPy import dif

sourceFolder = input("Please enter the source folder directory: ")

similarOrSame = input("Do you want to find the duplicates or similar images? D/S: ")
acceptedAnswersD = ["D", "d", "duplicate", "Duplicate"]
acceptedAnswersS = ["S", "s", "similar", "Similar"]
acceptedAnswersDS = acceptedAnswersD + acceptedAnswersS

while similarOrSame not in acceptedAnswersDS:
    print("You entered something invalid. Please try again")
    similarOrSame = input("Do you want to find the duplicates or similar images? D/S: ")

acceptedAnswersY = ["y", "yes", "Y", "Yes", "YES"]
acceptedAnswersN = ["n", "no", "N", "No", "NO"]
acceptedAnswersYN = acceptedAnswersY + acceptedAnswersN

if similarOrSame in acceptedAnswersD:
    keepPhotos = input("Do you want to keep the duplicates? Y/N: ")
    while keepPhotos not in acceptedAnswersYN:
        print("You entered something invalid. Please try again")
        keepPhotos = input("Do you want to keep the duplicates? Y/N: ")
    if keepPhotos in acceptedAnswersY:
        destinationFolder = input("Please enter the destination folder directory: ")
        search = dif(sourceFolder, move_to=destinationFolder)
    elif keepPhotos in acceptedAnswersN:
        search = dif(sourceFolder, show_output=True, delete=True)

elif similarOrSame in acceptedAnswersS:
    destinationFolder = input("Please enter the destination folder directory: ")
    search = dif(sourceFolder, similarity=1000, move_to=destinationFolder)