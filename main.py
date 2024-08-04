from flask import Flask, request, jsonify
import wikipedia

app = Flask(__name__)

# Initialize Wikipedia API
wiki_wiki = wikipedia
wiki_wiki.set_lang('en')


@app.route('/fetch_wikipedia', methods=['GET'])
def fetch_wikipedia():
    query = request.args.get('query')

    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    try:
        # Fetch data from Wikipedia
        page = wiki_wiki.page(title=query)
        if not page.exists():
            return jsonify({'error': 'No Wikipedia page found for this query'}), 404

        summary = page.summary
        return jsonify({'query': query, 'wikipedia_summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
