from api_client import *

def main():
    # Load existing credentials
    credentials = load_credentials()

    if credentials:
        username = credentials['username']
        password = credentials['password']
        apiKey = credentials['X-Api-Key']
        print("Found existing credentials. Attempting to log in...")
        token, refresh_token = login(username, password,apiKey)
        if token:
            print("Login successful.")
            while True:
                print("\nOptions:")
                print("1. See all available models by ID")
                print("2. Get Model by ID")
                print("3. Get Download file")
                print("4. Exit")
                choice = input("Choose an option (1-4): ")

                if choice == '1':
                    get_all_models(token,apiKey)
                elif choice == '2':
                    get_model_by_id(token,apiKey)
                elif choice == '3':
                    get_download_files(token,apiKey)
                elif choice == '4':
                    print("Exiting...")
                    break
                else:
                    print("Invalid option. Please try again.")
            return

        

    # If no credentials or login failed, register a new user
    print("No valid credentials found. Please contact usand request access at: support@humanscanrepository.com")

if __name__ == "__main__":
    main()