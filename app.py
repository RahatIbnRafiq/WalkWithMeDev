import streamlit as st
import wikipediaapi

# Set Wikipedia API object
wiki_wiki = wikipediaapi.Wikipedia('WalkWithMe (highlander.rahat@gmail.com)', 'en')

# Set the title of the web app
st.title("Wikipedia Search")

# Add a text input widget for search
search_query = st.text_input("Search for a topic:", value="")

# Display search results as the user types
if search_query:
    search_results = wiki_wiki.page(search_query).links
    search_results = [result.title for result in search_results.values()]

    # Create a selectbox for autocomplete suggestions
    selected_result = st.selectbox("Select a topic:", search_results)

    # Display information about the selected topic using Wikipedia API
    if selected_result:
        page = wiki_wiki.page(selected_result)
        if page.exists():
            st.write(f"Summary of {selected_result}:")
            st.write(page.summary)
        else:
            st.write(f"No information found for {selected_result}")

# JavaScript to update search results as the user types
js_code = """
<script>
document.addEventListener("input", function(event) {
  var userInput = event.target.value;
  var searchResults = document.getElementById("search-results");

  // Clear previous results
  while (searchResults.firstChild) {
    searchResults.removeChild(searchResults.firstChild);
  }

  if (userInput) {
    // Fetch and display search results from Wikipedia
    fetch("https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=" + userInput)
      .then(response => response.json())
      .then(data => {
        var suggestions = data[1];
        for (var i = 0; i < suggestions.length; i++) {
          var option = document.createElement("option");
          option.value = suggestions[i];
          searchResults.appendChild(option);
        }
      });
  }
});
</script>
"""

# Inject JavaScript code to enable dynamic autocomplete
st.markdown(js_code, unsafe_allow_html=True)
