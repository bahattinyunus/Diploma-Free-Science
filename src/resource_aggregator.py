class ResourceAggregator:
    def __init__(self):
        self.sources = ["arXiv", "DOAJ", "OpenAlex"]

    def search_papers(self, query):
        """
        Mock function to search for open access papers.
        In the future, this will connect to arXiv API.
        """
        print(f"Searching {self.sources} for: '{query}'...")
        
        # Mock results
        results = [
            {"title": f"Open Source Science in {query}", "author": "Doe, J.", "url": "http://arxiv.org/abs/1234.5678"},
            {"title": f"The Future of {query}", "author": "Smith, A.", "url": "http://arxiv.org/abs/8765.4321"}
        ]
        
        return results

if __name__ == "__main__":
    aggregator = ResourceAggregator()
    results = aggregator.search_papers("Quantum Computing")
    
    print("\n--- Results ---")
    for r in results:
        print(f"Title: {r['title']}")
        print(f"Link:  {r['url']}\n")
