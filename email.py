from flask import Blueprint, request, jsonify
from datetime import datetime
import json

email_bp = Blueprint('email', __name__)

# Mock email data
mock_emails = [
    {
        'id': 1,
        'sender': 'BaintNode',
        'subject': 'Node rewards ready',
        'preview': 'You have 12 BAINT pending. Claim now.',
        'content': 'Congratulations! Your node has produced 3 blocks this week and earned 12 BAINT tokens. Click here to claim your rewards.',
        'time': '2:30 PM',
        'read': False,
        'timestamp': datetime.now().isoformat()
    },
    {
        'id': 2,
        'sender': 'DAO Gov',
        'subject': 'Vote: Proposal #12',
        'preview': 'A proposal that affects storage fees',
        'content': 'Please review and vote on proposal #12 regarding the adjustment of storage fees for the network.',
        'time': '1:15 PM',
        'read': False,
        'timestamp': datetime.now().isoformat()
    },
    {
        'id': 3,
        'sender': 'BaintStore',
        'subject': 'New app: AgentKit',
        'preview': 'AgentKit is live on BaintStore',
        'content': 'AgentKit helps you deploy AI agents on the Baint network. Check it out in the BaintStore.',
        'time': '11:45 AM',
        'read': True,
        'timestamp': datetime.now().isoformat()
    }
]

@email_bp.route('/emails', methods=['GET'])
def get_emails():
    """Get all emails"""
    folder = request.args.get('folder', 'inbox')
    filter_type = request.args.get('filter', 'all')
    
    emails = mock_emails.copy()
    
    # Apply filters
    if filter_type == 'unread':
        emails = [email for email in emails if not email['read']]
    elif filter_type == 'starred':
        # For now, no starred emails
        emails = []
    
    return jsonify({
        'success': True,
        'emails': emails,
        'total': len(emails),
        'unread_count': len([e for e in mock_emails if not e['read']])
    })

@email_bp.route('/emails/<int:email_id>', methods=['GET'])
def get_email(email_id):
    """Get a specific email"""
    email = next((e for e in mock_emails if e['id'] == email_id), None)
    
    if not email:
        return jsonify({'success': False, 'error': 'Email not found'}), 404
    
    return jsonify({
        'success': True,
        'email': email
    })

@email_bp.route('/emails/<int:email_id>/read', methods=['POST'])
def mark_email_read(email_id):
    """Mark an email as read"""
    email = next((e for e in mock_emails if e['id'] == email_id), None)
    
    if not email:
        return jsonify({'success': False, 'error': 'Email not found'}), 404
    
    email['read'] = True
    
    return jsonify({
        'success': True,
        'message': 'Email marked as read'
    })

@email_bp.route('/emails/send', methods=['POST'])
def send_email():
    """Send a new email"""
    data = request.get_json()
    
    if not data or not data.get('to') or not data.get('subject'):
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400
    
    # Simulate sending email
    new_email = {
        'id': len(mock_emails) + 1,
        'sender': 'You',
        'subject': data.get('subject', 'No subject'),
        'preview': data.get('body', '')[:70] + '...' if len(data.get('body', '')) > 70 else data.get('body', ''),
        'content': data.get('body', ''),
        'time': 'Now',
        'read': True,
        'timestamp': datetime.now().isoformat(),
        'to': data.get('to')
    }
    
    mock_emails.insert(0, new_email)
    
    return jsonify({
        'success': True,
        'message': 'Email sent successfully',
        'email': new_email
    })

@email_bp.route('/emails/<int:email_id>/reply', methods=['POST'])
def reply_to_email(email_id):
    """Reply to an email"""
    data = request.get_json()
    original_email = next((e for e in mock_emails if e['id'] == email_id), None)
    
    if not original_email:
        return jsonify({'success': False, 'error': 'Original email not found'}), 404
    
    if not data or not data.get('body'):
        return jsonify({'success': False, 'error': 'Reply body is required'}), 400
    
    # Simulate reply
    reply_email = {
        'id': len(mock_emails) + 1,
        'sender': 'You',
        'subject': f"Re: {original_email['subject']}",
        'preview': data.get('body', '')[:70] + '...' if len(data.get('body', '')) > 70 else data.get('body', ''),
        'content': data.get('body', ''),
        'time': 'Now',
        'read': True,
        'timestamp': datetime.now().isoformat(),
        'to': original_email['sender']
    }
    
    mock_emails.insert(0, reply_email)
    
    return jsonify({
        'success': True,
        'message': 'Reply sent successfully',
        'email': reply_email
    })

@email_bp.route('/emails/search', methods=['GET'])
def search_emails():
    """Search emails"""
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify({'success': True, 'emails': [], 'total': 0})
    
    # Simple search in subject, sender, and content
    results = []
    for email in mock_emails:
        if (query in email['subject'].lower() or 
            query in email['sender'].lower() or 
            query in email['content'].lower()):
            results.append(email)
    
    return jsonify({
        'success': True,
        'emails': results,
        'total': len(results),
        'query': query
    })

@email_bp.route('/ai/smart-reply', methods=['POST'])
def generate_smart_reply():
    """Generate AI smart reply suggestions"""
    data = request.get_json()
    email_content = data.get('content', '') if data else ''
    
    # Mock smart reply suggestions
    suggestions = [
        "Thank you for the update!",
        "I'll review this and get back to you.",
        "Sounds good, let's proceed.",
        "Could you provide more details?",
        "I appreciate your help with this."
    ]
    
    return jsonify({
        'success': True,
        'suggestions': suggestions[:3]  # Return top 3 suggestions
    })

@email_bp.route('/ai/summarize', methods=['POST'])
def summarize_email():
    """Generate AI summary of email content"""
    data = request.get_json()
    email_content = data.get('content', '') if data else ''
    
    # Mock summarization
    summary = f"Summary: This email discusses {email_content[:50]}..." if email_content else "No content to summarize"
    
    return jsonify({
        'success': True,
        'summary': summary
    })

