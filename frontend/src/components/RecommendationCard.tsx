type Props = {
  title: string;
  description: string;
};

export default function RecommendationCard({ title, description }: Props) {
  return (
    <div className="recommendation-card">
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}


