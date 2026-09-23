import urllib.request

# Add any raw GitHub URLs or public tracker list endpoints here
SOURCES = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_i2p.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_yggdrasil_ip.txt",
    "https://tracker.adysec.com/trackers_all.txt",
    "https://tracker.adysec.com/trackers_best.txt",
    "https://tracker.adysec.com/trackers_best_http.txt",
    "https://tracker.adysec.com/trackers_best_https.txt",
    "https://tracker.adysec.com/trackers_best_udp.txt",
    "https://tracker.adysec.com/trackers_best_wss.txt",
    "https://raw.githubusercontent.com/kris3713/UltimateBTTrackersList/refs/heads/master/ultimate_trackers.txt",
    "https://raw.githubusercontent.com/xXSalamanderXx/salamander-trackers/refs/heads/main/combined.txt",
    "https://raw.githubusercontent.com/mrgusux/automatic-trackers/main/all_trackers.txt",
    "https://raw.githubusercontent.com/Sereinfy/TrackersList/main/main/output_trackers.txt",
    "https://raw.githubusercontent.com/Sereinfy/TrackersList/main/main/trackers.txt",
    "https://cf.trackerslist.com/best.txt",
    "https://cf.trackerslist.com/all.txt",
    "https://cf.trackerslist.com/http.txt",
    "https://cf.trackerslist.com/nohttp.txt",
]

def main():
    trackers = set()
    
    for url in SOURCES:
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as response:
                lines = response.read().decode('utf-8').splitlines()
                for line in lines:
                    cleaned = line.strip()
                    # Filter out comments, empty lines, and non-tracker entries
                    if cleaned and not cleaned.startswith('#'):
                        trackers.add(cleaned)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # Sort trackers alphabetically for a clean diff
    sorted_trackers = sorted(list(trackers))

    with open("trackers.txt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(sorted_trackers) + "\n")

    print(f"Successfully saved {len(sorted_trackers)} unique trackers.")

if __name__ == "__main__":
    main()
