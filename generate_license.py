""" Generates the IMAGES-LICENSES.md file from the images metadata.
"""
import os.path
import os
import json

if __name__ == "__main__":
    json_folder = 'info'
    output_file = 'IMAGES-LICENSES.md'
    json_fnames = [f for f in os.listdir(json_folder) 
                   if f.endswith('.json')]
    license_names = {
        'cc-3.0': "[CC BY 3.0](http://creativecommons.org/licenses/by/3.0/)",
        'cc-sa-3.0': "[CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/)",
        'cc-nd-3.0': "[CC BY-ND 3.0](http://creativecommons.org/licenses/by-nd/3.0/)",
        'cc-nc-3.0': "[CC BY-NC 3.0](http://creativecommons.org/licenses/by-nc/3.0/)",
        'cc-nc-sa-3.0': "[CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)",
        'cc-nc-nd-3.0': "[CC BY-NC-ND 3.0](http://creativecommons.org/licenses/by-nc-nd/3.0/)"
    }
    # Delete the license content.
    open(output_file, 'w').close()
    with open(output_file, 'w') as output:
        for json_fname in json_fnames:
            print json_fname
            with open(os.path.join(json_folder, json_fname)) as info_f:
                info = json.load(info_f)
                attribution = "'[{title}]({url})' by [{author}](http://{author}.deviantart.com) is licensed under {license}"
                formatted = attribution.format(
                    title=info['title'],
                    author=info['author'],
                    url=info['url'],
                    license=license_names[info['license_type']]
                )
                output.write(formatted + os.linesep)
                output.write(os.linesep)

