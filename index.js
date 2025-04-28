import Link from 'next/link';

export default function Home() {
  return (
    <div style={{ padding: 40, fontFamily: 'sans-serif' }}>
      <h1>🔗 PostGen ZA</h1>
      <Link href="/api/hello">
        <a>Test API → /api/hello</a>
      </Link>
      <br/>
      <button
        onClick={() => window.location.href = '/api/auth/linkedin'}
        style={{ marginTop: 20, padding: '10px 20px' }}
      >
        Connect with LinkedIn
      </button>
    </div>
  );
}
