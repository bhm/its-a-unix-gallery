from authentication import JsonCredentialsDescriptor
import click
from google_images import GoogleImageApiRepo
from os import path
import pprint
from remote_images import RemoteImage


@click.command()
@click.option('--query',
              metavar='<query>', show_default=True,
              help='What do we search for via Google Image Search')
@click.option('--json-credentials',
              metavar='json_credentials', show_default=True, default=JsonCredentialsDescriptor.DEFAULT_FILE_NAME,
              help="Json file with cx and developer key object")
def main(
        query,
        json_credentials
):
    if not path.exists(json_credentials):
        raise AttributeError('%s file does not exist' % json_credentials)

    descriptor = JsonCredentialsDescriptor(json_credentials)

    google_images_repo = GoogleImageApiRepo(descriptor)
    for link in google_images_repo.search_images(query):
        RemoteImage(link).open()
        pprint.pprint(link)


if __name__ == '__main__':
    main()
