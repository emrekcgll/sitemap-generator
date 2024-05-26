import csv
import math
import random


def generate_sitemap(urls, output_file, max_urls):
    num_sitemaps = math.ceil(len(urls) / max_urls)
    sitemap_list = []
    for i in range(num_sitemaps):
        start_idx = i * max_urls
        end_idx = (i + 1) * max_urls
        current_urls = urls[start_idx:end_idx]
        sitemap_name = f'{output_file}{i + 1}.xml'
        with open(sitemap_name, 'w') as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            for url in current_urls:
                priority = round(random.uniform(0.1, 1), 1)
                priority = str(priority)
                file.write('\t<url>\n')
                file.write(f'\t\t<loc>{url}</loc>\n')
                file.write(f'\t\t<lastmod>2024-03-15</lastmod>\n')
                file.write(f'\t\t<changefreq>always</changefreq>\n')
                file.write(f'\t\t<priority>{priority}</priority>\n')
                file.write('\t</url>\n')
            file.write('</urlset>')
        sitemap_list.append(sitemap_name)
    generate_sitemap_index(output_file + '.xml', sitemap_list)


def generate_sitemap_index(index_file, sitemaps):
    with open(index_file, 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for sitemap in sitemaps:
            file.write('\t<sitemap>\n')
            file.write(f'\t\t<loc>{sitemap}</loc>\n')
            file.write('\t</sitemap>\n')
        file.write('</sitemapindex>')


def read_urls_from_csv(csv_file):
    urls = []
    with open(csv_file, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            urls.append(row[0])
    return urls


if __name__ == "__main__":
    input_csv_file = 'urls.csv'
    urls = read_urls_from_csv(input_csv_file)
    max_urls_per_sitemap = 50000

    generate_sitemap(urls=urls, output_file='sitemap', max_urls=max_urls_per_sitemap)
    print(f"Sitemap and Sitemap Index files successfully created.")
