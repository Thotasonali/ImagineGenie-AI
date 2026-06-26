import { Sparkles } from 'lucide-react';

export function Header() {
  return (
    <header className="header">
      <div className="brand">
        <div className="brandIcon"><Sparkles size={24} /></div>
        <div>
          <h1>VisionForge AI</h1>
          <p>Enterprise AI creative platform</p>
        </div>
      </div>
      <div className="badge">Part 1 MVP</div>
    </header>
  );
}
