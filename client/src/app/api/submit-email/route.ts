import { google } from 'googleapis';
import { NextResponse } from 'next/server';
import path from 'path';
import fs from 'fs';

const credentialsPath = path.join(process.cwd(), process.env.GOOGLE_APPLICATION_CREDENTIALS || '');
const credentials = JSON.parse(fs.readFileSync(credentialsPath, 'utf8'));

const auth = new google.auth.GoogleAuth({
  credentials,
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