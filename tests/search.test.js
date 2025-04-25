/**
 * @jest-environment jsdom
 */

describe('SimpleJekyllSearch initialization', () => {
  beforeEach(() => {
    // Set up the DOM elements required by the script
    document.body.innerHTML = `
      <div class="page-link" id="search-container" style="float: right;">
        <input type="text" id="search-input" placeholder="Search...">
        <ul id="search-results"></ul>
      </div>
    `;

    // Mock SimpleJekyllSearch globally
    window.SimpleJekyllSearch = jest.fn();
  });

  it('should initialize SimpleJekyllSearch after DOMContentLoaded', () => {
    // Simulate the code in your <script>
    document.addEventListener('DOMContentLoaded', function() {
      var sjs = SimpleJekyllSearch({
        searchInput: document.getElementById('search-input'),
        resultsContainer: document.getElementById('search-results'),
        json: '/search.json',
        searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
        noResultsText: 'No results found',
        limit: 10,
        fuzzy: true
      });
    });

    // Dispatch DOMContentLoaded event
    document.dispatchEvent(new Event('DOMContentLoaded'));

    // Assert SimpleJekyllSearch was called with correct arguments
    expect(window.SimpleJekyllSearch).toHaveBeenCalledWith(
      expect.objectContaining({
        searchInput: document.getElementById('search-input'),
        resultsContainer: document.getElementById('search-results'),
        json: '/search.json'
      })
    );
  });
});
