import { google } from 'googleapis';
import { NextResponse } from 'next/server';

const auth = new google.auth.GoogleAuth({
  credentials: {
    type: process.env.GOOGLE_TYPE,
    project_id: process.env.GOOGLE_PROJECT_ID,
    private_key_id: process.env.GOOGLE_PRIVATE_KEY_ID,
    private_key: process.env.GOOGLE_PRIVATE_KEY.replace(/\\n/g, '\n'), // Replace escaped newlines
    client_email: process.env.GOOGLE_CLIENT_EMAIL,
    client_id: process.env.GOOGLE_CLIENT_ID,
    auth_uri: process.env.GOOGLE_AUTH_URI,
    token_uri: process.env.GOOGLE_TOKEN_URI,
    auth_provider_x509_cert_url: process.env.GOOGLE_AUTH_PROVIDER_CERT_URL,
    client_x509_cert_url: process.env.GOOGLE_CLIENT_CERT_URL,
  },
  scopes: ['https://www.googleapis.com/auth/spreadsheets'],
});

const sheets = google.sheets({ version: 'v4', auth });

export async function POST(req: Request) {
  try {
    const { email } = await req.json();
    
    await sheets.spreadsheets.values.append({
      spreadsheetId: process.env.GOOGLE_SHEET_ID,
      range: 'Sheet1!A:A',
      valueInputOption: 'USER_ENTERED',
      requestBody: {
        values: [[email]],
      },
    });

    return NextResponse.json({ message: 'Email submitted successfully' }, { status: 200 });
  } catch (error) {
    console.error('Error submitting email:', error);
    return NextResponse.json({ message: 'Error submitting email' }, { status: 500 });
  }
}
