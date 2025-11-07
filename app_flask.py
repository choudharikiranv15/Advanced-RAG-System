# app_flask.py - Simple Flask interface for RAG System
from flask import Flask, render_template, request, jsonify, session
import os
from werkzeug.utils import secure_filename
from config.config import Config
from src.rag_system import RAGSystem
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] = './data/pdfs'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Initialize RAG system
rag_system = RAGSystem(Config())

# Store conversation history per session
conversations = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file uploaded'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No file selected'})
    
    if not file.filename.endswith('.pdf'):
        return jsonify({'success': False, 'message': 'Only PDF files are allowed'})
    
    try:
        # Save file
        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process document
        result = rag_system.add_document(filepath)
        
        if result['success']:
            stats = result['statistics']
            return jsonify({
                'success': True,
                'message': f"Successfully added {result['document_name']}",
                'statistics': stats
            })
        else:
            return jsonify({'success': False, 'message': result['message']})
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '').strip()
    
    if not question:
        return jsonify({'success': False, 'message': 'Please enter a question'})
    
    try:
        # Get or create conversation history for this session
        session_id = session.get('session_id')
        if not session_id:
            session_id = secrets.token_hex(8)
            session['session_id'] = session_id
        
        if session_id not in conversations:
            conversations[session_id] = []
        
        # Get response
        response = rag_system.query(question, conversations[session_id])
        
        # Update conversation history
        conversations[session_id].append(question)
        conversations[session_id].append(response['answer'])
        
        return jsonify({
            'success': True,
            'answer': response['answer'],
            'metadata': {
                'sources_used': response.get('sources_used', 0),
                'confidence': response.get('confidence', 0),
                'query_type': response.get('query_type', 'unknown')
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/clear', methods=['POST'])
def clear_conversation():
    session_id = session.get('session_id')
    if session_id and session_id in conversations:
        conversations[session_id] = []
    rag_system.clear_conversation_history()
    return jsonify({'success': True})

@app.route('/stats', methods=['GET'])
def get_stats():
    try:
        stats = rag_system.get_system_stats()
        return jsonify({'success': True, 'stats': stats})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    print("🚀 Starting RAG System with Flask...")
    print("📝 Note: Using simple vector store (no ChromaDB issues)")
    print("🌐 Open your browser at: http://localhost:8080")
    app.run(host='127.0.0.1', port=8080, debug=False)
