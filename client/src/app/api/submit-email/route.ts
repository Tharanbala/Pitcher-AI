import { google } from 'googleapis';
import { NextResponse } from 'next/server';

interface Credentials {
  type: string;
  project_id: string;
  private_key_id: string;
  private_key: string;
  client_email: string;
  client_id: string;
  auth_uri: string;
  token_uri: string;
  auth_provider_x509_cert_url: string;
  client_x509_cert_url: string;
}

const credentials: Credentials = {
  type: process.env.GOOGLE_TYPE as string,
  project_id: process.env.GOOGLE_PROJECT_ID as string,
  private_key_id: process.env.GOOGLE_PRIVATE_KEY_ID as string,
  private_key: process.env.GOOGLE_PRIVATE_KEY?.replace(/\\n/g, '\n') as string,
  client_email: process.env.GOOGLE_CLIENT_EMAIL as string,
  client_id: process.env.GOOGLE_CLIENT_ID as string,
  auth_uri: process.env.GOOGLE_AUTH_URI as string,
  token_uri: process.env.GOOGLE_TOKEN_URI as string,
  auth_provider_x509_cert_url: process.env.GOOGLE_AUTH_PROVIDER_CERT_URL as string,
  client_x509_cert_url: process.env.GOOGLE_CLIENT_CERT_URL as string,
};

const auth = new google.auth.GoogleAuth({
  credentials,
  scopes: ['https://www.googleapis.com/auth/spreadsheets'],
});

const sheets = google.sheets({ version: 'v4', auth });

export async function POST(req: Request) {
  try {
    const { email } = await req.json();
    
    await sheets.spreadsheets.values.append({
      spreadsheetId: process.env.GOOGLE_SHEET_ID as string,
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
